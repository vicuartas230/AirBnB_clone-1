#!/usr/bin/python3
""" State Module for HBNB project """
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ
import models


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete")

    if environ['HBNB_TYPE_STORAGE'] != 'db':
        @property
        def cities(self):
            """ returns the list of City instances with
                state_id equals to the current State.id """
            list_cities = []
            for k, v in models.storage.all(City).items():
                if self.id == v.state_id:
                    list_cities.append(v)
            return list_cities
