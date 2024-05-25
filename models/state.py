#!/usr/bin/python3
""" State Module for HBNB project """
from os import environ

from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
import models

# from models.city import City


class State(BaseModel, Base):
    """State class"""

    if environ.get("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """cities list"""
            result = []
            for city in models.storage.all(models.city.City).values():
                if city.state_id == self.id:
                    result.append(city)
            return result
