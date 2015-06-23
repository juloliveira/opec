__version__ = '0.0.1'

from bottle import Bottle, TEMPLATE_PATH
from app import settings

opec = Bottle()
TEMPLATE_PATH.insert(0, settings.TEMPLATE_PATH)
from app.controllers import *   # NOQA
