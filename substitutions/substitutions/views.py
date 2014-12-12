from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    )


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def index(request):
    items = [
        {
            'title': 'Pizza',
            'dollars': '3',
            'cents': '88',
            'img': 'static/images/digiorno-pizza.jpg',
            'id': '1'
        },
        {
            'title': 'Bread',
            'dollars': '3',
            'cents': '88',
            'img': 'static/images/digiorno-pizza.jpg',
            'id': '2'
        },
        {
            'title': 'Milk',
            'dollars': '3',
            'cents': '88',
            'img': 'static/images/digiorno-pizza.jpg',
            'id': '3'
        },
        {
            'title': 'Pizza',
            'dollars': '3',
            'cents': '88',
            'img': 'static/images/digiorno-pizza.jpg',
            'id': '4'
        },
        {
            'title': 'Bread',
            'dollars': '3',
            'cents': '88',
            'img': 'static/images/digiorno-pizza.jpg',
            'id': '5'
        },
        {
            'title': 'Milk',
            'dollars': '3',
            'cents': '88',
            'img': 'static/images/digiorno-pizza.jpg',
            'id': '6'
        },
        {
            'title': 'Pizza',
            'dollars': '3',
            'cents': '88',
            'img': 'static/images/digiorno-pizza.jpg',
            'id': '7'
        },
        {
            'title': 'Bread',
            'dollars': '3',
            'cents': '88',
            'img': 'static/images/digiorno-pizza.jpg',
            'id': '8'
        },
        {
            'title': 'Milk',
            'dollars': '3',
            'cents': '88',
            'img': 'static/images/digiorno-pizza.jpg',
            'id': '9'
        },
        {
            'title': 'Pizza',
            'dollars': '3',
            'cents': '88',
            'img': 'static/images/digiorno-pizza.jpg',
            'id': '10'
        },
        {
            'title': 'Bread',
            'dollars': '3',
            'cents': '88',
            'img': 'static/images/digiorno-pizza.jpg',
            'id': '11'
        },
        {
            'title': 'Milk',
            'dollars': '3',
            'cents': '88',
            'img': 'static/images/digiorno-pizza.jpg',
            'id': '12'
        }
    ]

    return { 'items': items };

@view_config(route_name='item', renderer='templates/item.pt')
def item(request):
    item = { 
            'title': 'Pizza',
            'url': 'http://www.pizzamarket.net/images/pizza2.jpg',
            'id': '1'
        }      

    substitutions = [
        {
            'title': 'Pizza',
            'url': 'http://www.pizzamarket.net/images/pizza2.jpg',
            'id': '1'
        },
        {
            'title': 'Bread',
            'url': 'http://www.pizzamarket.net/images/pizza2.jpg',
            'id': '2'
        },
        {
            'title': 'Milk',
            'url': 'http://www.pizzamarket.net/images/pizza2.jpg',
            'id': '3'
        }
    ]

    return { 'item': item, 'substitutions': substitutions };
