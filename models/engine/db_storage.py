#!/usr/bin/python3
""" This script defines a class DBStorage """
from models.base_model import Base
from sqlalchemy import (create_engine)
from os import environ


class DBStorage():
    """ This class defines attributes and methods """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}\
'.format(environ['HBNB_MYSQL_USER'], environ['HBNB_MYSQL_PWD\
'], environ['HBNB_MYSQL_HOST'], environ['HBNB_MYSQL_DB'], pool_pre_ping=True)
    Base.metadata.create_all(self.__engine)
    if environ['HBNB_ENV'] == 'test':
        Base.metadata.drop_all(engine)

    def all(self, cls=None):
