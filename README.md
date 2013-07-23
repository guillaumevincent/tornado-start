Tornado-start
=============

Introduction
------------
Tornado_start is a template for building a Tornado web application in 5 minutes.

Author
------
[Guillaume Vincent](guillaumevincent.com)

Requirements
------------
*  python v2.7.x (python --version)
*  pip 1.3.x (pip --version)
*  virtualenv 1.9.x (virtualenv --version)

Start
-----
All you have to do is to:

*  clone this repository 

    __git clone https://github.com/guillaumevincent/tornado-start.git YOUR_APPLICATION_NAME__

*  move into YOUR_APPLICATION_NAME folder

    __cd YOUR_APPLICATION_NAME/__

*  rename tornado-start folder by YOUR_APPLICATION_NAME

    __mv tornado-start/ YOUR_APPLICATION_NAME/__

*  rename APPLICATION_NAME = 'YOUR_APPLICATION_NAME' in settings.py

*  rename import in runserver.py

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
*  you can add some python libraries you use in requirements.txt
*  configure your deploy/fabfile.py file for deployment in production
