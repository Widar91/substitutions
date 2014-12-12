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
