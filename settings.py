import os
import uuid
import base64
import logging.config
from config.config import Config

APPLICATION_NAME = '$your_application_name'

PROJECT_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(PROJECT_DIR, APPLICATION_NAME, 'templates')
STATIC_DIR = os.path.join(PROJECT_DIR, 'static')
CONFIG_FILE = os.path.join(PROJECT_DIR, 'config', 'config.ini')

config = Config()
config.read(CONFIG_FILE)

DEBUG = config.get_boolean(APPLICATION_NAME, 'debug', False)
LOGIN_URL = config.get_option(APPLICATION_NAME, 'login_url', '/login/')
PORT = config.get_int(APPLICATION_NAME, 'port', 8000)

if config.has_option(APPLICATION_NAME, 'cookie_secret'):
    COOKIE_SECRET = config.get(APPLICATION_NAME, 'cookie_secret')
else:
    COOKIE_SECRET = base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
    if not config.has_section(APPLICATION_NAME):
        config.add_section(APPLICATION_NAME)
    config.set(APPLICATION_NAME, 'cookie_secret', COOKIE_SECRET)
    with open(CONFIG_FILE, 'wt') as cf:
        config.write(cf)

LOGGING_FILE = os.path.join(PROJECT_DIR, 'logs', 'logging.json')
logging.config.dictConfig(LOGGING_FILE)
