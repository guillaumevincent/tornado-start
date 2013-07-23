Tornado-start
=============

Introduction
------------
Tornado-start is the directory layout I used for my Tornado applications.
I try to make it simple, and I use it for my Tornado projects.

Requirements
------------
python v2.7.x (python --version)
tornado v3.x.x (pip freeze | grep tornado)
pip 1.3.x (pip --version)
virtualenv 1.9.x (virtualenv --version)

Start
-----
All you have to do is to:

*  clone this repository
*  rename $your_application_name folder by your application name
*  rename APPLICATION_NAME = '$your_application_name' in settings.py
*  rename $your_application_name in logs/logging.json file

Make virtualenv
---------------

*  mkdir ~/.env/
*  cd ~/.env/
*  virtualenv $your_application_name