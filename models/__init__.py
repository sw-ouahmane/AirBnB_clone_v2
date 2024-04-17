#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.base_model import BaseModel
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import environ
from models.engine.file_storage import FileStorage
from models.engine.db_storageold import DBStorage


storage_engine = environ.get("HBNB_TYPE_STORAGE")

storage = DBStorage() if storage_engine == "db" else FileStorage()
storage.reload()
