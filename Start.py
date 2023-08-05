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
      conn = get_db_connection()

      restaurants = conn.execute('SELECT * FROM restaurants').fetchall()
      conn.close()
      
      # check if hotel is present in the list
      for rest in restaurants:
      	if rest['restaurant_title'] == rest_name:
      		restaurant_found = rest
      		break

      if restaurant_found == None:
      	return redirect(url_for('add_restaurant_menu', name = rest_name))      	
      else:
      	dict = {'Tea':50,'Coffee':60,'Toast':70}
      	return render_template("restaurant_menu.html", result = dict, name = rest_name)
      	

# To load the list of restaurant
@app.route('/restaurant_list')
def restaurant_list():
	conn = get_db_connection()

	dict_restaurants = conn.execute('SELECT * FROM restaurants').fetchall()
	conn.close()

	return render_template("restaurant_list.html", results = dict_restaurants)


# To load the page for adding fresh menue for a restaurant
@app.route('/add_menu/<name>')
def add_restaurant_menu(name):
	return render_template("add_menu.html", rest_name = name )

@app.route('/create', methods=('GET', 'POST'))
def add_rest_menu():
	if request.method == 'POST':
		title = request.form['title']
		cost = request.form['cost']
		restaurant_id = request.form['rest_id']

		if not title:
			flash('Title/Cost is required!')
		else:
			conn = get_db_connection()
			conn.execute('INSERT INTO menus (item_title, item_cost, item_restaurant_id) VALUES (?, ?)',(title, cost, restaurant_id))
			conn.commit()
			conn.close()
			return redirect(url_for('index'))

	return render_template('create.html')
  


def get_db_connection():
	conn = sqlite3.connect("freemenu_database.db")
	conn.row_factory = sqlite3.Row
	return conn


# The route() decorator in Flask is used to bind URL to a function
@app.route('/hello')
def helloworld():
   return 'hello world .'

if __name__ == '__main__':
	app.debug = True
	app.run()	
	# app.run(debug = True)