from app import opec


@opec.route('/', method='GET')
def index():
    return "Hello World"
