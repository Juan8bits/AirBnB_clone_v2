#!/usr/bin/python3
""" New engine """
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base

user = os.getenv("HBNB_MYSQL_USER")
passwd = os.getenv("HBNB_MYSQL_PWD")
host = os.getenv("HBNB_MYSQL_HOST")
data_b = os.getenv("HBNB_MYSQL_DB")
hbnb_env = os.getenv("HBNB_ENV")


class DBStorage():
    """ Engine """
    __engine = None
    __session = None

    def __init__(self):
        """ Constructor method that create a session and engine """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, data_b),
                                      pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        if (hbnb_env == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Method that return a dictionary with all cls objects
            or if cls is None, all objects in the database.
        """
        dic_ob = {}
        info = self.__session.query(State, City).all()  # Make sure!
        if cls is None:
            for i in info:
                for j in i:
                    dic_ob[j.__class__.__name__ + '.' + j.id] = j
        else:
            for i in info:
                for j in i:
                    print("{} == a {}".format(j.__class__.__name__, cls))
                    if (j.__class__.__name__ == cls):
                        dic_ob[j.__class__.__name__ + '.' + j.id] = j
        return dic_ob

    def new(self, obj):
        """ Add the object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commit all changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Method that delete from the current database
            session obj if not None.
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Reload objects from DB"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
