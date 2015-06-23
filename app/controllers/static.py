from bottle import static_file
from app import opec


@opec.get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')


@opec.get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')


@opec.get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/img')


@opec.get('/fonts/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/fonts')


@opec.get('/bootstrap/js/<filename:re:.*\.js>')
def bootstrap_javascript(filename):
    return static_file(filename, root='static/bootstrap/dist/js')


@opec.get('/bootstrap/css/<filename:re:.*\.(css|map)>')
def bootstrap_stylesheets(filename):
    return static_file(filename, root='static/bootstrap/dist/css')

"""
@opec.get('/bootstrap/images/<filename:re:.*.(jpg|png|gif|ico)>')
 def bootstrap_images(filename):
    return static_file(filename, root='static/bootstrap/dist/css')
"""


@opec.get('/bootstrap/css/<filename:re:.*\.(eot|ttf|woff|svg)>')
def bootstrap_fonts(filename):
    return static_file(filename, root='static/bootstrap/dist/fonts')
