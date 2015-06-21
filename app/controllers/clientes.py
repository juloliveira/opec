from app import opec


@opec.route('/clientes')
def clientes():
    return "Clientes"
