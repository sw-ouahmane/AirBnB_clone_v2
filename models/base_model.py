#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
from os import environ
from uuid import uuid4
from datetime import datetime
from sqlalchemy import Column, String, DateTime
import models
from sqlalchemy.ext.declarative import declarative_base

s = environ.get("HBNB_TYPE_STORAGE")

Base = declarative_base() if s == "db" else object


class BaseModel:
    """
    Base class to define all common attributes and methods for
    other classes
    """

    id = Column(String(60), primary_key=True, nullable=False)
    now = datetime.utcnow()
    created_at = Column(DateTime, nullable=False, default=now)
    updated_at = Column(DateTime, nullable=False, default=now)

    def __init__(self, *args, **kwargs):
        """
        initialization of BaseModel
        """
        if kwargs:
            for key in kwargs:
                if key == "__class__":
                    continue
                elif key in ("created_at", "updated_at"):
                    setattr(
                        self,
                        key,
                        datetime.strptime(kwargs[key], "%Y-%m-%dT%H:%M:%S.%f"),
                    )
                else:
                    setattr(self, key, kwargs[key])
                self.id = str(uuid4())
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()

    def __str__(self):
        """
        return string representation of a Model
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        update latest updation time of a model
        """
        self.updated_at = datetime.now()
        if environ.get("HBNB_TYPE_STORAGE") != "db":
            models.storage.new(self)
            models.storage.save()

    def to_dict(self):
        """
        custom representation of a model
        """
        output_dict = {}
        output_dict.update({"__class__": self.__class__.__name__})
        for key in self.__dict__.keys():
            if key in ("created_at", "updated_at"):
                output_dict.update({key: getattr(self, key).isoformat()})
            elif key == "_sa_instance_state":
                continue
            else:
                output_dict.update({key: getattr(self, key)})
        return output_dict

    def delete(self):
        """delete the current instance from the storage"""
        key: str = f"{self.__class__.__name__}.{self.id}"
        del models.storage.__objects[key]
