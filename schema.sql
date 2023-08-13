
DROP TABLE IF EXISTS restaurants;
DROP TABLE IF EXISTS menus;

CREATE TABLE restaurants (
    rest_id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    restaurant_title TEXT NOT NULL,
    restaurant_location TEXT NOT NULL
);


CREATE TABLE menus (
    menu_id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    item_title TEXT NOT NULL,
    item_cost TEXT NOT NULL,
    item_restaurant_id INTEGER REFERENCES restaurants (rest_id)
);


