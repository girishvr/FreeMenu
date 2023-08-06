# init_db.py

import sqlite3

connection = sqlite3.connect('freemenu_database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO restaurants (restaurant_title, restaurant_location) VALUES (?, ?)",
            ('Test', 'Nowhere')
            )

cur.execute("INSERT INTO restaurants (restaurant_title, restaurant_location) VALUES (?, ?)",
            ('Royal', 'Hotel Royal, Hyderabad')
            )

cur.execute("INSERT INTO restaurants (restaurant_title, restaurant_location) VALUES (?, ?)",
            ('Sunrise', 'Hotel Sunrise, Delhi')
            )

cur.execute("INSERT INTO menus (item_title,item_cost,item_restaurant_id) VALUES (?, ?, ?)",
            ('Green Tea', '10', 2)
            )

cur.execute("INSERT INTO menus (item_title,item_cost,item_restaurant_id) VALUES (?, ?, ?)",
            ('Black Tea', '20', 2)
            )

cur.execute("INSERT INTO menus (item_title,item_cost,item_restaurant_id) VALUES (?, ?, ?)",
            ('Herbal Tea', '30', 2)
            )

cur.execute("INSERT INTO menus (item_title,item_cost,item_restaurant_id) VALUES (?, ?, ?)",
            ('Coffee', '50', 3)
            )

cur.execute("INSERT INTO menus (item_title,item_cost,item_restaurant_id) VALUES (?, ?, ?)",
            ('Black Coffee', '40', 3)
            )

connection.commit()
connection.close()