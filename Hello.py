#Hello.py
#First file for Flask project

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'

# The route() decorator in Flask is used to bind URL to a function
@app.route('/hello')
def helloworld():
   return 'hello world'

if __name__ == '__main__':
	# app.debug = True
	app.run()	
	# app.run(debug = True)