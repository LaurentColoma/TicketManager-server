# Ticket Manager:
## Server side:

### Introduction
This is the backend of a ticket managing web-application.
It has been developed using Django [Django](https://www.djangoproject.com/), a high level [Python](https://www.python.org/) framework.
### Licence
The entire code is under the [MIT](https://en.wikipedia.org/wiki/MIT_License) licence, you are totally free to re-use it for whatever purpose you want.
### Installation
#### - Prerequisites:
Beforehand, It would be better if you check if you have any package that need an update.
````bash
sudo apt update
sudo apt upgrade
````
Also don't forget to clone!
````bash
git clone https://github.com/LaurentColoma/TicketManager-server.git
````

##### 1 - Postgresql
You can now start by installing and setting up **Postgresql**
````bash
sudo apt install postgresql postgresql-contrib
````
Check if everything is running well.
````
service postgresql status
````
You should get something like this: 
````
● postgresql.service - PostgreSQL RDBMS
   Loaded: loaded (/lib/systemd/system/postgresql.service; enabled; vendor preset: enabled)
   Active: active (exited) since jeu. 2018-11-01 11:43:54 CET; 4h 0min ago
 Main PID: 28135 (code=exited, status=0/SUCCESS)
    Tasks: 0
   Memory: 0B
      CPU: 0
   CGroup: /system.slice/postgresql.service

nov. 01 11:43:54 $your_computer_name systemd[1]: Starting PostgreSQL RDBMS...
nov. 01 11:43:54 $your_computer_name systemd[1]: Started PostgreSQL RDBMS.
nov. 01 11:43:58 $your_computer_name systemd[1]: Started PostgreSQL RDBMS.
````
You can now launch postgres.
````
sudo -i -u postgres
psql
````
Your terminal should display the following: 
````bash
psql (9.5.14)
Type "help" for help.

postgres=#
````
Then you will create a *User* and a *Database*, it will be needed for the good usage of the backend.

**Creating a User**
````sql
postgres=# CREATE USER $your_user_name WITH PASSWORD '$your_password';
CREATE ROLE
````
> The usage of the simple quote around  $your_password and the semi-colon at the end of each request is very important

**Creating a Database**
````sql
postgres=# CREATE DATABASE $your_database_name;
CREATE DATABASE
````
Congratulations, you should have manage to create your user and your database.
To quit psql and postgresql just do:
````sql
\q
exit
````
Before going further, you need to update a file according to the different elements you have just created.
*~/server/Components/settings.py*
Your modification will take place from line 89 to 98:
````python
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': 'tracker',
		'USER': 'laurent',
		'PASSWORD': 'azerty',
		'HOST': '127.0.0.1',
		'PORT': '5432',
	}
}
````

You have to change the value of **NAME**, **USER** and **PASSWORD**  with the user and database we made earlier
````python
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql',
		'NAME': '$your_database_name',
		'USER': '$your_username',
		'PASSWORD': '$your_password',
		'HOST': '127.0.0.1',
		'PORT': '5432',
	}
}
````

##### 2-Virtualenv
The server need to run inside a virtual environment, allong with the server, we provide a [virtualenv](https://virtualenv.pypa.io/en/latest/) already set for the server.
Just launch it!
````bash
source ~server/virtualenv/bin/activate
````
You need to create an admin user for the server now.
````bash
sudo ./manage.py createsuperuser
Username: $your_username
Email address: $your_email@example.com
Password: **********
Password (again): **********
Superuser created successfully
````
Now you just have to update and then launch the server.
````bash
sudo ./manage.py migrate
sudo ./manage.py runserver
````
You should get something like this at this point
````
/usr/local/lib/python2.7/dist-packages/psycopg2/__init__.py:144: UserWarning: The psycopg2 wheel package will be renamed from release 2.8; in order to keep installing from binary please use "pip install psycopg2-binary" instead. For details see: <http://initd.org/psycopg/docs/install.html#binary-install-from-pypi>.
  """)
/usr/local/lib/python2.7/dist-packages/psycopg2/__init__.py:144: UserWarning: The psycopg2 wheel package will be renamed from release 2.8; in order to keep installing from binary please use "pip install psycopg2-binary" instead. For details see: <http://initd.org/psycopg/docs/install.html#binary-install-from-pypi>.
  """)
Performing system checks...

System check identified some issues:

WARNINGS:
tracker.Ticket.consulted_set: (fields.W340) null has no effect on ManyToManyField.
tracker.Ticket.informed_set: (fields.W340) null has no effect on ManyToManyField.
tracker.Ticket.module_set: (fields.W340) null has no effect on ManyToManyField.
tracker.Ticket.version_affected_set: (fields.W340) null has no effect on ManyToManyField.

System check identified 4 issues (0 silenced).
November 01, 2018 - 15:09:47
Django version 1.11, using settings 'Components.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
````
Don't worry about the error, it's not on your side, we still need to correct some minor thing!
Just navigate to *http://127.0.0.1:8000/* or *http://127.0.0.1:8000/admin*
to see the result of your installation.

Feedback appreciated.
