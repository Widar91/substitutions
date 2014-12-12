from pyramid.response import Response
from pyramid.view import view_config

from sqlalchemy.exc import DBAPIError

from .models import (
    DBSession,
    MyModel,
    )


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
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


conn_err_msg = """\
Pyramid is having a problem using your SQL database.  The problem
might be caused by one of the following things:

1.  You may need to run the "initialize_substitutions_db" script
    to initialize your database tables.  Check your virtual
    environment's "bin" directory for this script and try to run it.

2.  Your database server may not be running.  Check that the
    database server referred to by the "sqlalchemy.url" setting in
    your "development.ini" file is running.

After you fix the problem, please restart the Pyramid application to
try it again.
"""

