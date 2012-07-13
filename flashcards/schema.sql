CREATE TABLE IF NOT EXISTS decks (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	deck_title CHAR(100) NOT NULL,
	public BOOL NOT NULL
);

CREATE TABLE IF NOT EXISTS cards (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	card_data CHAR(100) NOT NULL,
	card_number INTEGER NOT NULL,
	assoc_deck INTEGER NOT NULL
);

INSERT OR IGNORE INTO decks (id, deck_title, owner) VALUES (1, "Home", 1)
INSERT OR IGNORE INTO decks (id, deck_title, owner) VALUES (2, "Air Force", 1)
INSERT OR IGNORE INTO cards (id, card_data, card_number, assoc_deck) VALUES (1, "table", 1, 1)
INSERT OR IGNORE INTO cards (id, card_data, card_number, assoc_deck) VALUES (2, "chair", 2, 1)
INSERT OR IGNORE INTO cards (id, card_data, card_number, assoc_deck) VALUES (3, "coin", 1, 2)
INSERT OR IGNORE INTO cards (id, card_data, card_number, assoc_deck) VALUES (4, "commander", 2, 2)



