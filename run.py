from bottle import run
from logging import info
from app import opec


def main():
    info('opec started')
    run(opec)

if __name__ == '__main__':
    main()
