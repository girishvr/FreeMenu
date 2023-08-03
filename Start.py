#Start.py
#First file for Flask project

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	dict = {'Tea':50,'Coffee':60,'Toast':70}
	return render_template("index.html", name = "Darling", result = dict)

# The route() decorator in Flask is used to bind URL to a function
@app.route('/hello')
def helloworld():
   return 'hello world .'

if __name__ == '__main__':
	app.debug = True
	app.run()	
	# app.run(debug = True)