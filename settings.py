import os
import uuid
import base64
import logging.config
from config.config import Config

APPLICATION_NAME = '$YOUR_APPLICATION_NAME'

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

LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(process)d - %(thread)d - %(message)s',
            'datefmt': '%d/%m/%Y %Hh%Mm%Ss'
        },
        'simple': {
            'format': '%(asctime)s - %(name)-12s - %(levelname)-8s - %(message)s',
            'datefmt': '%d/%m/%Y %Hh%Mm%Ss'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'stream': 'ext://sys.stdout'
        },
        'info_file_handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'INFO',
            'formatter': 'simple',
            'filename': 'logs/info.log',
            'maxBytes': '10485760',
            'backupCount': '5',
            'encoding': 'utf8'
        },
        'error_file_handler': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'ERROR',
            'formatter': 'verbose',
            'filename': 'logs/errors.log',
            'maxBytes': '10485760',
            'backupCount': '5',
            'encoding': 'utf8'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console', 'info_file_handler', 'error_file_handler'],
            'level': 'INFO',
            'propagate': True
        }
    }
}

LOGGING_DIR = os.path.join(PROJECT_DIR, 'logs')
if not os.path.isdir(LOGGING_DIR):
    os.makedirs(LOGGING_DIR)
logging.config.dictConfig(LOGGING_CONFIG)
