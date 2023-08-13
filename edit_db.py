# init_db.py

import sqlite3

connection = sqlite3.connect('freemenu_database.db')


# with open('schema.sql') as f:
#     connection.executescript(f.read())

cur = connection.cursor()

# cur.execute("DELETE FROM restaurants WHERE rest_id = 1")


# cur.execute("INSERT INTO restaurants (restaurant_title, restaurant_location, restaurant_phone) VALUES (?, ?, ?)",
#             ('Test', 'Nowhere', "9876543210")
#             )

# cur.execute("INSERT INTO menus (item_title,item_cost,item_restaurant_id) VALUES (?, ?, ?)",
#             ('Black Coffee', '40', 3)
#             )

cur.execute("UPDATE restaurants SET restaurant_title='Cafe Girish' WHERE rest_id = 4")


connection.commit()
connection.close()