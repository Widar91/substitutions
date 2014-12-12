import requests
from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from substitutions.models.item import Item

@view_config(route_name='home', renderer='templates/list.pt')
def list(request):
    items = Item.getBySkuList(['3000113008','3000012265','3000052730','1020660','3000039841','3000052189','1020383','3000358008','1000137','3000055130','1007213','1013221','3000687121','1003222'])
    return { 'items': items };

@view_config(route_name='item', renderer='templates/item.pt')
def item(request):
    skuId = request.matchdict['skuId']
    item = Item.getBySkuId(skuId)

    # query the collaborative filtering model here
    #r = requests.get('http://localhost:5000/predict/{0}'.format(skuId))
    #result = r.json()
    
    #skuList = [x["sku"] for x in result["prediction"]]

    substitutions = []#Item.getBySkuList(skuList)

    return { 'item': item, 'substitutions': substitutions };
