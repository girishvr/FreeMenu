#app.py
#First file for Flask project
import sqlite3
from flask_qrcode import QRcode
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

QRcode(app)

# TODO - Change this
app.secret_key = 'Free-Menu-GVR2003MANDVI'

@app.route('/')
def index():
	print("Index Page")
	return render_template("index.html", name = "Darling")



@app.route('/restaurant_menu',methods = ['POST', 'GET'])
def restaurant_menu_result():
	if request.method == 'POST':
		result = request.form
		rest_name = result["rest_name"] 
		
		restaurant_found = get_restaurant_by_name(rest_name)
		
		if restaurant_found == None:
			# Show Alert
			msg = f"Please Enter Restaurant Name! Or ADD A NEW RESTAURANT"
			if len(rest_name) > 0:
				msg = f"Restauran Not Found! Try ADD NEW RESTAURANT"

			flash(msg)
			return redirect(url_for('index'))       
			# Stay on the same page         
			# return (''), 204      
		else:
			dict = get_menu_for_restaurant(rest_id = restaurant_found['rest_id'])         
			# print_sqlite_object(dict)
			return render_template("restaurant_menu.html", result = dict, name = rest_name)
			
	# implemented without exception handling - to be optimised later     
	if request.method == 'GET':            

		rest_id = request.args.get('rest_id')
		rest_name = request.args.get("rest_name")

		dict = get_menu_for_restaurant(rest_id = rest_id)
		# print_sqlite_object(dict)
		return render_template("restaurant_menu.html", result = dict, name = rest_name)
	
			
@app.route('/get_menu/<name>')
def get_restaurant_menu(name):

	print("get_menu called with " + name)

	restaurant_found = get_restaurant_by_name(name)
	if restaurant_found == None:
		return redirect(url_for('get_restaurant_menu', name = "Test"))       
	else:
		dict = get_menu_for_restaurant(rest_id = restaurant_found['rest_id'])         
		return render_template("get_menu.html", result = dict, name = name)

	# Stay on the same page         
	return (''), 204


# To load the list of restaurant
@app.route('/restaurant_list')
def restaurant_list():

	print("List All restaurant")
	restaurants = get_all_restaurants()
	
	return render_template("restaurant_list.html", results = restaurants)



# To load the page for adding fresh menue for a restaurant
@app.route('/add_menu/<name>')
def add_restaurant_menu(name):
	return render_template("add_menu.html", rest_name = name )


@app.route('/create_new', methods=('GET', 'POST'))
def create_new_rest():
	if request.method == 'POST':

		rest_name = request.form['rest_name']
		restaurant_loc = request.form['restaurant_loc']

		if not rest_name:
			flash('restaurant name/restaurant location is required!')
		else:
			save_new_restaurant(rest_name, restaurant_loc)
			flash("New Restaurant Added")
			return redirect(url_for('restaurant_list'))

	return (''), 204


# Method saves list of menu items sent from table - /add_menu page
@app.route('/create_menu/<rest_name>', methods=('GET', 'POST'))
def add_rest_menu(rest_name):
		
	data = request.form
	
	if request.method == 'POST':
		# Get list of items and costs
		item_list = data.getlist('title')
		cost_list = data.getlist('cost')

		# Check if restaurant exists
		restaurant_found = get_restaurant_by_name(rest_name)

		if restaurant_found != None:

			item_restaurant_id = restaurant_found['rest_id']

			# One by one add menue items
			for i in range(len(item_list)):

				item_title = item_list[i]
				item_cost = cost_list[i]
			
				if not item_title or not item_cost:
					flash('Title/Cost is required!')
					break
				else:
					save_menu_items(item_title, item_cost, item_restaurant_id)

			# for loop end	
		
		#Load Restaurant page with the menu
		flash("Menu Item(s) Saved")
		return redirect(url_for('restaurant_menu_result', rest_name = rest_name, rest_id = item_restaurant_id))       

		# return render_template("restaurant_menu.html", result = dict, name = rest_name)
		# return redirect(url_for('get_restaurant_menu', name = rest_name))       

	return (''), 204


# ----------------------------------------------------------------------------------- #
# ---------------------------- QR CODE Generate ------------------------------------- #
# ----------------------------------------------------------------------------------- #


@app.route('/get_qr/<rest_name>',methods = ['POST', 'GET'])	
def get_qr(rest_name):

	print(rest_name)

	restaurant_link = request.url_root + "get_menu/" + rest_name
	print(restaurant_link)

	return render_template('get_qr.html', rest_link=restaurant_link, rest_name = rest_name)

	  
# TODO - to delete/edit menu or restaurants
#For later - delete an item
@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
	 post = get_post(id)
	 conn = get_db_connection()
	 conn.execute('DELETE FROM posts WHERE id = ?', (id,))
	 conn.commit()
	 conn.close()
	 flash('"{}" was successfully deleted!'.format(post['title']))
	 return redirect(url_for('index'))

# ------------------------------------------------------------------------------------------------ #
# ------------ DB calls -------------------------------------------------------------------------- #
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

def save_new_restaurant(rest_name, restaurant_loc):
	conn = get_db_connection()
	conn.execute('INSERT INTO restaurants (restaurant_title, restaurant_location) VALUES (?, ?)',(rest_name, restaurant_loc))
	conn.commit()
	conn.close()


def save_menu_items(title, cost, restaurant_id):
	conn = get_db_connection()
	conn.execute('INSERT INTO menus (item_title, item_cost, item_restaurant_id) VALUES (?,?,?)',(title, cost, restaurant_id))
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

def get_restaurant_by_name(rest_name):
	restaurant_found = None
	restaurants = get_all_restaurants()

	# check if hotel is present in the list
	for rest in restaurants:
		if rest['restaurant_title'] == rest_name:
			restaurant_found = rest
			break

	return restaurant_found         

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