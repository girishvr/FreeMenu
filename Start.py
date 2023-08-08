#Start.py
#First file for Flask project
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def index():
	
	return render_template("index.html", name = "Darling")


@app.route('/restaurant_menu',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      rest_name = result["rest_name"]
      restaurant_found = None
      restaurants = get_all_restaurants()

      
      # check if hotel is present in the list
      for rest in restaurants:
      	if rest['restaurant_title'] == rest_name:
      		restaurant_found = rest
      		break

      if restaurant_found == None:
      	return redirect(url_for('add_restaurant_menu', name = rest_name))      	
      else:
      	dict = get_menu_for_restaurant(rest_id = restaurant_found['rest_id'])      	
      	print_sqlite_object(dict)
      	return render_template("restaurant_menu.html", result = dict, name = rest_name)
      	

# To load the list of restaurant
@app.route('/restaurant_list')
def restaurant_list():

	restaurants = get_all_restaurants()
	
	return render_template("restaurant_list.html", results = restaurants)


# To load the page for adding fresh menue for a restaurant
@app.route('/add_menu/<name>')
def add_restaurant_menu(name):
	return render_template("add_menu.html", rest_name = name )


# TODO - finish this 
@app.route('/create', methods=('GET', 'POST'))
def add_rest_menu():
	if request.method == 'POST':

		title = request.form['title']
		cost = request.form['cost']
		restaurant_id = request.form['rest_id']

		if not title:
			flash('Title/Cost is required!')
		else:
			save_menu_items(item_title, item_cost, item_restaurant_id)
			# return redirect(url_for('index'))

	# return render_template('create.html')
	return (''), 204
  
# ------------------------------------------------------------------------------------------------ #
# ------------ DB calls ---------------- #
# ------------------------------------------------------------------------------------------------ #


def get_db_connection():
	conn = sqlite3.connect("freemenu_database.db")
	conn.row_factory = sqlite3.Row
	return conn


def get_all_restaurants():
	conn = get_db_connection()

	# Works - use this query for search operation

	# rest_name = "s"
	# sql = f"""SELECT * FROM restaurants WHERE restaurant_title LIKE '%{rest_name}%'"""
	# restaurants = conn.execute(sql).fetchall()

	restaurants = conn.execute('SELECT * FROM restaurants').fetchall()

	conn.close()

	return restaurants


def save_menu_items(item_title, item_cost, item_restaurant_id):
	conn = get_db_connection()
	conn.execute('INSERT INTO menus (item_title, item_cost, item_restaurant_id) VALUES (?, ?)',(title, cost, restaurant_id))
	conn.commit()
	conn.close()


def get_menu_for_restaurant(rest_id):
	conn = get_db_connection()
	
	# menus = conn.execute('SELECT * FROM menus').fetchall()	
	sql = f"""SELECT * FROM menus WHERE item_restaurant_id = {rest_id}"""
	menus = conn.execute(sql).fetchall()	

	conn.close()

	return menus






# =============================================================

# Using a custom factory to get row results as a pure dictionary.

def dict_factory(cursor, row):
	d = {}
	for idx, col in enumerate(cursor.description):
		d[col[0]] = row[idx]

	return d	


def print_sqlite_object(objs):
	for item in objs:
		print(item)
		for column in item:
			print(column)

# =============================================================

# The route() decorator in Flask is used to bind URL to a function
@app.route('/hello')
def helloworld():
   return 'hello world .'


#START of the program
if __name__ == '__main__':
	app.debug = True
	app.run()	
	# app.run(debug = True)