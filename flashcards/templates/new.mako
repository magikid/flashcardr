# -*- coding: utf-8 -*- 
<%inherit file="layout.mako" />

<h1>Add a new card</h1>

<form action="${request.route_url('new')}" method="post">
  <input type="text" maxlength="100" name="card_data">
  <input type="hidden" name="assoc_deck" value="${deck['id']}">
  <input type="submit" name="add" value="ADD" class="button">
</form>
