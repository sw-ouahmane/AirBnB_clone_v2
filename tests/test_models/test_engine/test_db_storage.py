#!/usr/bin/python3
"""DB storage module
"""
<<<<<<< HEAD
    tests for FileStorage
"""
import unittest
from models.engine.db_storage import DBStorage
from sqlalchemy.engine.base import Engine
=======

from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from models.base_model import Base
from models.city import City
from models.review import Review
from models.state import State
from models.user import User
from models.place import Place
from models.amenity import Amenity

HBNB_MYSQL_USER = getenv("HBNB_MYSQL_USER")
HBNB_MYSQL_PWD = getenv("HBNB_MYSQL_PWD")
HBNB_MYSQL_HOST = getenv("HBNB_MYSQL_HOST")
HBNB_MYSQL_DB = getenv("HBNB_MYSQL_DB")
>>>>>>> fac2c91d666fd3ea5463a2a30762d737479b9d6a


class DBStorage:
    """database storage for mysql conversion"""

    __engine = None
    __session = None

    def __init__(self):
        """initializer"""
        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(
                HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB
            ),
            pool_pre_ping=True,
        )
        env = getenv("HBNB_ENV")
        if env == "test":
            Base.metadata.create_all(self.__engine)

    def all(self, cls=None):
        """list all instances of cls"""
        result = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            for row in self.__session.query(cls).all():
                key = f"{cls.__name__}.{row.id}"
                result.update({key: row})
        else:
            classes_dict = {
                "states": State,
                "cities": City,
                "users": User,
                "places": Place,
                "reviews": Review,
                "amenities": Amenity,
            }
            for table in classes_dict.values():
                cls = classes_dict[table]
                for row in self.__session.query(cls).all():
                    key = f"{cls.__name__}.{row.id}"
                    result.update({key: row})
        return result

    def new(self, obj):
        """add object to current database session"""
        self.__session.add(obj)

    def save(self):
        """commit current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete an element in the table"""
        if obj:
            self.session.delete(obj)

    def reload(self):
        """create database session"""

        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

    def close(self):
        """close scoped session"""
        self.__session.close()