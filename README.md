Tornado-start
=============

Introduction
------------
Tornado-start is a template for building a Tornado web application.


Requirements
------------
*  python v2.7.x (python --version)
*  pip 1.3.x (pip --version)
*  virtualenv 1.9.x (virtualenv --version)

Start
-----
All you have to do is to:

*  clone this repository (git clone https://github.com/guillaumevincent/tornado-start.git **$YOUR_APPLICATION_NAME**)
*  move into **$YOUR_APPLICATION_NAME** folder (cd **$YOUR_APPLICATION_NAME**/)
*  rename **tornado-start** folder by **$YOUR_APPLICATION_NAME** (mv tornado-start/ **$YOUR_APPLICATION_NAME**/)
*  rename APPLICATION_NAME = '**$YOUR_APPLICATION_NAME**' in settings.py

Make a virtualenv
-----------------
*  mkdir ~/.env/
*  virtualenv ~/.env/**$YOUR_APPLICATION_NAME**/
*  . ~/.env/**$YOUR_APPLICATION_NAME**/bin/activate
*  pip install tornado

You are ready to go
-------------------
*  python runserver.py

