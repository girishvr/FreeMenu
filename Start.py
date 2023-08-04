#Start.py
#First file for Flask project

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
	
	return render_template("index.html", name = "Darling")


@app.route('/restaurant_menu',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      rest_name = result["rest_name"]
      
      restaurants = ['Test','Royal','Sunrise']

      # check if hotel is present in the list
      if rest_name in restaurants:
      	dict = {'Tea':50,'Coffee':60,'Toast':70}
      	return render_template("restaurant_menu.html", result = dict, name = rest_name)
      else:
      	return redirect(url_for('add_restaurant_menu', name = rest_name))



@app.route('/add_menu/<name>')
def add_restaurant_menu(name):

	return render_template("add_menu.html", rest_name = name )



# The route() decorator in Flask is used to bind URL to a function
@app.route('/hello')
def helloworld():
   return 'hello world .'

if __name__ == '__main__':
	app.debug = True
	app.run()	
	# app.run(debug = True)