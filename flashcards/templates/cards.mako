# -*- coding: utf-8 -*- 
<%inherit file="layout.mako" />
<h1>Cards</h1>

<ul id="cards">
% if cards:
	%for card in cards:
	<li>
		<span class="card_number">${card['card_number']}</span>
		<span class="card_data">${card['card_data']}</span>	
	</li>
	% endfor
%else:
	<li>There are no cards</li>
%endif
<li class="last">
	<a href="${request.route_url('new")}">Add a new card</a>
</li>
</ul>
