#!/usr/bin/python
import numpy as np
import re
from collections import defaultdict
import os.path
from flask import Flask, jsonify

def load_data(purchase, subs):
    users = {}
    products = {}
    for user, product in purchase:
        if user not in users:
            users[user] = len(users)
        if product not in products:
            products[product] = len(products)
    P = np.zeros((len(products), len(users)))
    for user, product in purchase:
        P[products[product], users[user]] = 1
    m = defaultdict(lambda:(0,0))
    for product1, product2, accepted in subs:
        if product1 not in products or product2 not in products:
            continue
        p1 = products[product1]
        p2 = products[product2]
        n, d = m[(p1, p2)]
        d += 1
        if accepted:
            n += 1
        m[(p1, p2)] = (n, d)
    S = np.empty((len(products), len(products)))
    S[:] = np.nan
    for (p1, p2), (n, d) in m.items():
        S[p1, p2] = n / float(d)
    return P, S, users, products

def similarity(A):
    s = np.dot(A, A.T)
    square_mag = np.diag(s)
    inv_square_mag = 1. / square_mag
    inv_square_mag[np.isinf(inv_square_mag)] = 0
    inv_mag = np.sqrt(inv_square_mag)
    cosine = s * inv_mag
    cosine = cosine.T * inv_mag
    return cosine

def sub(x, y, subs, sim):
    indices = np.nonzero(subs[x, :] >= 0)[0]
    result = np.dot(sim[y, indices], subs[x, indices]) / float(indices.size)
    return result

def sub1(x, y, subs, sim):
    if subs[x, y] >= 0:
        return subs[x, y]
    i1 = np.nonzero(subs[x, :] >= 0)[0]
    i2 = np.nonzero(subs[:, y] >= 0)[0]
    num = np.dot(sim[y, i1], subs[x, i1]) + np.dot(sim[i2, x], subs[i2, y])
    den = np.sum(sim[y, i1]) + np.sum(sim[i2, x])
    return num / den

def load(purchase, substitution):
    P, S, users, products = load_data(purchase, substitution)
    sim = similarity(P)
    return { "sim": sim, "sub": S, "users": users, "products": products, "inverse_users": { v: k for k, v in users.items() }, "inverse_products": { v: k for k, v in products.items() } }

class Model():
    def __init__(self, path=""):
        self.sim = np.load(os.path.join(path, "sim.npy"))
        self.subs = np.load(os.path.join(path, "subs.npy"))
        self.products = load_dict(os.path.join(path, "products"))
        self.skus, self.categories = build_taxo(read_taxo(os.path.join(path, "taxo.csv")))
        self.inverse_products = { v: k for k, v in self.products.items() }

    def get_sku(self, product):
        return dict(self.skus[product])

    def predict(self, product, k=None):
        sku = self.skus[product]
        category = sku["category"]
        candidates = self.categories[category]
        p = self.products[product]
        result = np.zeros(len(self.products))
        for c in candidates:
            if c not in self.products:
                continue
            i = self.products[c]
            if i == p:
                continue
            result[i] = sub(p, i, self.subs, self.sim)
        out = [{ "sku": self.inverse_products[x], "title": self.skus[self.inverse_products[x]]["title"], "score": result[x], "similarity": self.sim[p, x], "substitution": None if np.isnan(self.subs[p, x]) else self.subs[p, x] } for x in np.argsort(result)[::-1] if x != p and result[x] > 0 and x]
        if k is not None:
            out = out[:k]
        return out

r = re.compile(r"^\"(\d+)\",\"(\d+)\"\n$")
def read_purchase(name):
    for i, line in enumerate(open(name)):
        if i > 1000000:
            break
        match = r.match(line)
        if match:
            profile_id = int(match.group(1))
            sku_id = int(match.group(2))
            yield profile_id, sku_id

r1 = re.compile(r"^(\d+),\"(\d+)\",\"([a-zA-Z]+)\"\n$")
def read_subs(name):
    for i, line in enumerate(open(name)):
        match = r1.match(line)
        if match:
            product1_id = int(match.group(1))
            product2_id = int(match.group(2))
            access = match.group(3) == "TRUE"
            yield product1_id, product2_id, access

r2 = re.compile(r"^\"(\d+)\",\"([^\"]+)\",\"([^\"]+)\"\n$")
def read_taxo(name):
    for i, line in enumerate(open(name)):
        if i == 0:
            continue
        match = r2.match(line)
        if match:
            sku_id = match.group(1)
            title = match.group(2)
            category = match.group(3)
            yield sku_id, title, category

def build_taxo(taxo_data):
    skus = {}
    categories = defaultdict(set)
    for sku_id, title, category in taxo_data:
        skus[sku_id] = { "title": title, "category": category }
        categories[category].add(sku_id)
    return skus, categories

def save_dict(f, d):
    ff = open(f, "w")
    for k, v in d.items():
        ff.write("{0},{1}\n".format(k, v))
    ff.close()

def load_dict(f):
    d = {}
    for line in open(f):
        k, v = line.strip().split(",")
        d[k] = int(v)
    return d

def make_it():
    P, S, users, products = load_data(list(read_purchase("user_sku.csv")), list(read_subs("subs.csv")))
    sim = similarity(P)
    np.save("sim", sim)
    np.save("subs", S)
    save_dict("users", users)
    save_dict("products", products)
    print "user: {0}, products: {1}".format(len(users), len(products))

def display(x):
    s = []
    for k, v in x.items():
        s.append("{0}={1}".format(k, v))
    return ", ".join(s)

def fetch(model, sku):
    print model.get_sku(sku)["title"]
    for result in model.predict(sku, k=10):
        print "   {0}".format(result["title"])

# make_it()

app = Flask(__name__)
model = Model()

@app.route('/predict/<sku>', methods=['GET'])
def get_tasks(sku):
    product = model.get_sku(sku)
    product["sku"] = sku
    return jsonify({ "product": product, "prediction": model.predict(sku, k=10) })

if __name__ == '__main__':
    app.run(debug=True)