__version__ = '0.0.1'

from bottle import Bottle

opec = Bottle()
from app.controllers import *
