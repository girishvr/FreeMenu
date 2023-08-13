#! /bin/bash

#source venv/bin/activate
#python3 app.py

echo "Updating the files..."
git pull origin master

echo "Restarting the server..."
sudo service apache2 restart

echo "Recent logs:"

sudo tail -50 /var/log/apache2/error-5000.log
sudo tail -50 /var/log/apache2/access-5000.log

echo "Build complete."