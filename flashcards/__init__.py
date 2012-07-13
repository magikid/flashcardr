import os
from pyramid.config import Configurator

here = os.path.dirname(os.path.abspath(__file__))

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_route('decks', '/')
    config.add_route('cards', '/deck/{id}')
    config.add_route('new', '/deck/{id}/new')
    config.add_static_view('static', os.path.join(here, 'static'))
    config.scan()

    return config.make_wsgi_app()
