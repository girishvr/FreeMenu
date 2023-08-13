# FreeMenu
Free Menu Application For Restaurants

## This is a free menue project build using Flask 

## First time setup on the system
	- pip3 install Flask
	- pip3 install Flask-QRcode
	- pip3 install virtualenv
	- pip3 install gunicorn
	- virtualenv venv

## Steps to set up database
	Python3 init_db.py

## Steps to run the application

### 1. Go to the FreeMenu folder
	cd FreeMenu

### 2. Set up Flask Environment - install virtualenv for development environment		
	source venv/bin/activate
	gunicorn -b 0.0.0.0:5000 app:app

### 3. Run the application 
	Python3 app.py

## Direct Build - script written in build.sh file

	./build.sh

------------------------------------------------------------------------------------------------

### Ref - Intial Set up
	https://www.tutorialspoint.com/flask/flask_application.htm

### Ref - Databse and rerouting set up
	https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

### Ref - For Deployment on Apache
	https://jqn.medium.com/deploy-a-flask-app-on-aws-ec2-1850ae4b0d41

<!-- Resources -->
<!-- Button -->

### Ref - Custom Buttons
	https://htmlcssfreebies.com/pheasant-demure-buttons

<!-- Button -->
### Ref - Custom Alert
	https://silverboxjs.ir/

<!-- QR Code -->
### Ref - QR Code
	 https://marcoagner.github.io/Flask-QRcode/
