Tornado-start
=============

Introduction
------------
Tornado-start is a template for building a Tornado web application in 5 minutes.

Author
------
[Guillaume Vincent](guillaumevincent.com)

Requirements
------------
*  python v2.7
*  pip 1.3
*  virtualenv 1.9

Start
-----
All you have to do is to:

*  clone this repository 

    git clone https://github.com/guillaumevincent/tornado-start.git PROJECT_DIR_NAME

*  move into PROJECT_DIR_NAME folder

    cd PROJECT_DIR_NAME/

*  rename tornado_start folder by YOUR_APPLICATION_NAME

    mv tornado_start/ YOUR_APPLICATION_NAME/

*  rename APPLICATION_NAME = 'YOUR_APPLICATION_NAME' in settings.py

*  rename import in runserver.py

    from tornado_start.handlers import Index

    become

    from YOUR_APPLICATION_NAME.handlers import Index

Make a virtualenv
-----------------
*  mkdir ~/.env/
*  virtualenv ~/.env/YOUR_APPLICATION_NAME/
*  . ~/.env/YOUR_APPLICATION_NAME/bin/activate
*  pip install -r requirements.txt

And run tornado server
-------------------
*  python runserver.py

Tests
-----
Add some test_xxx.py files in test folder and run tests with runtests.py

Go further
----------
you can :

*  add some python libraries you use in requirements.txt
*  configure your deploy/fabfile.py file for deployment in production
*  add some alias in your .profile:

    alias venvYOUR_APPLICATION_NAME='. ~/.env/YOUR_APPLICATION_NAME/bin/activate'

    alias cdYOUR_APPLICATION_NAME='. ~/workspace/YOUR_APPLICATION_NAME/'

License
-------
Tornado-start is under MIT License.
See LICENSE for more information