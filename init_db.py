# init_db.py

import sqlite3

connection = sqlite3.connect('freemenu_database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO restaurants (restaurant_title, restaurant_location, restaurant_phone) VALUES (?, ?, ?)",
            ('Some Place Nice', 'Nowhere', '8787878789')
            )

cur.execute("INSERT INTO restaurants (restaurant_title, restaurant_location, restaurant_phone) VALUES (?, ?, ?)",
            ('Royal', 'Hotel Royal, Hyderabad', '9898985600')
            )

cur.execute("INSERT INTO restaurants (restaurant_title, restaurant_location, restaurant_phone) VALUES (?, ?, ?)",
            ('Sunrise', 'Hotel Sunrise, Delhi', '9988773300')
            )

cur.execute("INSERT INTO menus (item_title,item_cost,item_restaurant_id) VALUES (?, ?, ?)",
            ('Green Tea', '10', 1)
            )

cur.execute("INSERT INTO menus (item_title,item_cost,item_restaurant_id) VALUES (?, ?, ?)",
            ('Black Tea', '20', 1)
            )

cur.execute("INSERT INTO menus (item_title,item_cost,item_restaurant_id) VALUES (?, ?, ?)",
            ('Herbal Tea', '30', 1)
            )

cur.execute("INSERT INTO menus (item_title,item_cost,item_restaurant_id) VALUES (?, ?, ?)",
            ('Roti', '10', 2)
            )

cur.execute("INSERT INTO menus (item_title,item_cost,item_restaurant_id) VALUES (?, ?, ?)",
            ('Daal', '30', 2)
            )

cur.execute("INSERT INTO menus (item_title,item_cost,item_restaurant_id) VALUES (?, ?, ?)",
            ('Rice - Plain', '30', 2)
            )


cur.execute("INSERT INTO menus (item_title,item_cost,item_restaurant_id) VALUES (?, ?, ?)",
            ('Coffee', '50', 3)
            )

cur.execute("INSERT INTO menus (item_title,item_cost,item_restaurant_id) VALUES (?, ?, ?)",
            ('Black Coffee', '40', 3)
            )

connection.commit()
connection.close()