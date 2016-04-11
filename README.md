## todolist

A simple todo list built in django. The application uses bootstrap, Ajax and MySQL database. 
* **Implement Features:**
  - Login
  - Logout
  - Add task
  - List tasks
  - Check a task (mark as solved)

# Getting Started
* **Prerequisites:**
  - [Python version 2.7](https://www.python.org/downloads/release/python-2711/)
  - [Django version 1.9](https://www.djangoproject.com/download/)
  - [MySQL database](http://dev.mysql.com/doc/refman/5.7/en/installing.html)
  
* **How to run the project:**
  - Clone or Download this repository. 
  - Install the project dependencies.
  	- pip install -r requirements.txt in your root project folder.
  - Setup the DATABASE conf
  	- Create MySQL option file '[db.conf]'(https://github.com/Salma7amed/todolist/blob/master/db.cnf.dist) in home directory
  - Create the new models in the app
  	- python manage.py makemigrations tasks
  - Run database migrate
  	- python manage.py migrate
  - Run the project
  	- python manage.py runserver
  - See the project running on localhost
  	- 127.0.0.1:8000
