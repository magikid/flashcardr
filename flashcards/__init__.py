
import os
import logging
import sqlite3

from pyramid.config import Configurator
from pyramid.events import NewRequest
from pyramid.events import subscriber
from pyramid.events import ApplicationCreated
from pyramid.exceptions import NotFound
from pyramid.httpexceptions import HTTPFound

@subscriber(ApplicationCreated)
def application_created_subscriber(event):
	log.warn('Initializing database...')
	f = open(os.path.join(here, 'schema.sql'), 'r')
	stmt = f.read()
	settings = event.app.registry.settings
	db = sqlite3.connect(settings['db'])
	db.executescript(stmt)
	db.commit()
	f.close()

@subscriber(NewRequest)
def new_request_subscriber(event):
	request = event.request
	settings = request.registry.settings
	request.db = sqlite3.connect(settings['db'])
	request.add_finished_callback(close_db_connection)

def close_db_connection(request):
	request.db.close()


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
	settings['db'] = os.path.join(here, 'tasks.db')
	
    config = Configurator(settings=settings)
    config.add_route('decks', '/')
    config.add_route('cards', '/deck/{id}')
    config.add_route('new', '/deck/{id}/new')
    config.add_static_view('static', os.path.join(here, 'static'))
    config.scan()

    return config.make_wsgi_app()
