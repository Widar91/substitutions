from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from substitutions.models.item import Item

@view_config(route_name='home', renderer='templates/list.pt')
def list(request):
    items = Item.get(12)
    return { 'items': items };

@view_config(route_name='item', renderer='templates/item.pt')
def item(request):
    skuId = request.matchdict['skuId']
    item = Item.getBySkuId(skuId)

    # query the collaborative filtering model here
    substitutions = Item.getBySkuList(('2','1','5','4','3'))

    return { 'item': item, 'substitutions': substitutions };
