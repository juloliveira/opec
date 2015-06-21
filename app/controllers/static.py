from bottle import static_file
from app import opec


@opec.get('/<filename:re:.*\.js')
def javascripts(filename):
    return static_file(filename, root='static/js')


@opec.get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')


@opec.get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/img')


@opec.get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/fonts')
