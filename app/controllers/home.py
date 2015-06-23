from bottle import template
from app import opec


@opec.route('/', method='GET')
def index():
    return template('index')
