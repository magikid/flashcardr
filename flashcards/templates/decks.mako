# -*- coding: utf-8 -*- 
<%inherit file="layout.mako" />
<h1>Decks</h1>

<ul id="decks">
% if decks:
	%for deck in decks:
	<li>
		<span class="deck_title">${deck['deck_title']}</span>
		<span class="actions">
			[ <a href="${request.route_url('cards', id=deck['id'])}">Open</a> ]
		</span>
	</li>
	% endfor
%else:
	<li>There are no decks</li>
%endif
</ul>
