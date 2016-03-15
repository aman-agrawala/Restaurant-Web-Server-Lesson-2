# Restaurant-Web-Server-Lesson-2
This code is for a simple local webserver written in python that displays restaurants and their respective menu items.
This project will eventually move from using BaseHTTPServer in Python to Flask.

In order to get this code up and running, it is expected that you are familiar with Python, and SQLAlchemy. Please see https://www.python.org/ for more information on installing and setting up python by yourself. Please see http://docs.sqlalchemy.org/en/rel_1_0/core/tutorial.html for setting up SQLAlchemy. Furthermore, it is advised to install vagrant on your own machine to get all additional programs quickly intsalled. Please see this link for more details on this process: https://www.udacity.com/wiki/ud197/install-vagrant.

## Instructions

1. Open up terminal/Git Bash and cd to you vagrant folder.

2. Type `vagrant up` and, after the virtual machine is turned on, type `vagrant ssh` to login

3. Type `cd /vagrant` to go to common directory and then cd into your Restaurant-Web-Server-Lesson2 folder.

4. Now type `python restaurantserver.py` and hit enter.

5. The server should be running locally at `localhost:8080` and you can view it yourself by typing `localhost:8080/restaurants` into your browser url bar.

You can now edit, delete, or create new restaurants and their menu items. If you would like to select a different port for your website, then open up the finalProject.py file and scroll all the way to the last line. By changing the value of port in `app.run(host='0.0.0.0', port=8000)` you can select any port you prefer. 
