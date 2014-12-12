import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from substitutions.item import (
    Item,
    DBSession,
    Base
    )

def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)

    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
    with transaction.manager:
        DBSession.add(Item(skuId='1', title='Pizza', url='http://upload.wikimedia.org/wikipedia/commons/1/10/Hot_pizza.jpg'))
        DBSession.add(Item(skuId='2', title='Milk', url='http://upload.wikimedia.org/wikipedia/commons/1/10/Hot_pizza.jpg'))
        DBSession.add(Item(skuId='3', title='Bread', url='http://upload.wikimedia.org/wikipedia/commons/1/10/Hot_pizza.jpg'))
        DBSession.add(Item(skuId='4', title='Pig', url='http://upload.wikimedia.org/wikipedia/commons/1/10/Hot_pizza.jpg'))
        DBSession.add(Item(skuId='5', title='Cheese', url='http://upload.wikimedia.org/wikipedia/commons/1/10/Hot_pizza.jpg'))
        DBSession.add(Item(skuId='6', title='Celery', url='http://upload.wikimedia.org/wikipedia/commons/1/10/Hot_pizza.jpg'))
        DBSession.add(Item(skuId='7', title='Apple', url='http://upload.wikimedia.org/wikipedia/commons/1/10/Hot_pizza.jpg'))
        DBSession.add(Item(skuId='8', title='Sandwhich', url='http://upload.wikimedia.org/wikipedia/commons/1/10/Hot_pizza.jpg'))
