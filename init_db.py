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

# cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
#             ('Second Post', 'Content for the second post')
#             )

connection.commit()
connection.close()