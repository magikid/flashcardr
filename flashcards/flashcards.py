
import os
import logging
import sqlite3

from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from pyramid.events import NewRequest
from pyramid.events import subscriber
from pyramid.events import ApplicationCreated
from pyramid.exceptions import NotFound
from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config

from wsgiref.simple_server import make_server

logging.basicConfig()
log = logging.getLogger(__file__)

here = os.path.dirname(os.path.abspath(__file__))

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

if __name__ == '__main__':
	settings['db'] = os.path.join(here, 'tasks.db')
	settings['mako.directories'] = os.path.join(here, 'templates')
	
	session_factory = UnencryptedCookieSessionFactoryConfig('itsaseekreet')
	
	config = Configurator(settings=settings, session_factory=session_factory)
	config.add_route('decks', '/')
	config.add_route('cards', '/deck/{id}')
	config.add_route('new', '/deck/{id}/new')
	config.add_static_view('static', os.path.join(here, 'static'))
	config.scan()

	app = config.make_wsgi_app()
	server = make_server('0.0.0.0', 8080, app)
	server.serve_forever()
