#!/usr/bin/python3
"""This is the amenity module."""
from os import environ


from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity Class"""

    if environ.get("HBNB_TYPE_STORAGE") == "db":
        from models.place import place_amenity

        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place", secondary=place_amenity, back_populates="amenities"
        )
    else:
        name = ""
