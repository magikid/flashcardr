from pyramid.view import view_config
	
@view_config(route_name='decks', renderer='decks.mako')
def deck_view(request):
        rs = request.db.execute("select id,deck_title from decks where public = 1")
        decks = [dict(id=row[0], deck_title=row[1]) for row in rs.fetchall()]
        return {'decks': decks}

@view_config(route_name='cards', renderer='cards.mako')
def card_view(request):
        deck_id = int(request.matchdict['id'])
        rs = request.db.execute("select card_number,card_data from cards where assoc_deck = ?", [deck_id])
        cards = [dict(card_number=row[0], card_data=row[1]) for row in rs.fetchall()]
        return {'cards': cards}

@view_config(route_name='new', renderer='new.mako')
def new_view(request):
        deck_id = int(request.matchdict['id'])
        if request.method == 'POST':
                if request.POST.get('card_data'):
                        request.db.execute('insert into cards (card_data, assoc_deck) VALUES (?, ?)', [request.POST['card_data'], deck_id])
                        request.db.commit()
                        request.session.flash('Added card!')
                        return HTTPFound(location=request.route_url('decks'))
                else:
                        request.session.flash("You didn't add any data!")
        return {}


@view_config(context='pyramid.exceptions.NotFound', renderer='notfound.mako')
def notfound_view(self):
        return {}

