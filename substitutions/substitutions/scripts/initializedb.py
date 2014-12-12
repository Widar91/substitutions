import os
import sys
import transaction

from sqlalchemy import engine_from_config

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from substitutions.models.item import (
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
        DBSession.add(Item('1', 'Pizza', 'http://upload.wikimedia.org/wikipedia/commons/1/10/Hot_pizza.jpg'))
        DBSession.add(Item('2', 'Bread', 'http://upload.wikimedia.org/wikipedia/commons/1/1f/FD_1.jpg'))
        DBSession.add(Item('3', 'Apple', 'http://upload.wikimedia.org/wikipedia/commons/1/10/Hot_pizza.jpg'))
        DBSession.add(Item('4', 'Cheese', 'http://upload.wikimedia.org/wikipedia/commons/1/10/Hot_pizza.jpg'))
        DBSession.add(Item('5', 'Hotdogs', 'http://upload.wikimedia.org/wikipedia/commons/1/10/Hot_pizza.jpg'))
        DBSession.add(Item('6', 'Celery', 'http://upload.wikimedia.org/wikipedia/commons/1/10/Hot_pizza.jpg'))
        DBSession.add(Item('7', 'Chicken', 'http://upload.wikimedia.org/wikipedia/commons/1/10/Hot_pizza.jpg'))
        DBSession.add(Item('8', 'Baked Beans', 'http://upload.wikimedia.org/wikipedia/commons/1/10/Hot_pizza.jpg'))
        DBSession.add(Item('9', 'Oranges', 'http://upload.wikimedia.org/wikipedia/commons/1/10/Hot_pizza.jpg'))
        DBSession.add(Item('10', 'Fish', 'http://upload.wikimedia.org/wikipedia/commons/1/10/Hot_pizza.jpg'))
        DBSession.add(Item('11', 'Pasta', 'http://upload.wikimedia.org/wikipedia/commons/1/10/Hot_pizza.jpg'))
        DBSession.add(Item('12', 'Sauce', 'http://upload.wikimedia.org/wikipedia/commons/1/10/Hot_pizza.jpg'))
