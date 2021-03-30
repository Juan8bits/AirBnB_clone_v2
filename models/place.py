#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), nullable=False, ForeignKey("cities.id"))
    user_id = Column(String(60), nullable=False, ForeignKey("users.id"))
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Colums(Integer, nullable=False, default=0)
    number_bathrooms = Colums(Integer, nullable=False, default=0)
    max_guest = Colums(Integer, nullable=False, default=0)
    price_by_night = Colums(Integer, nullable=False, default=0)
    latitude = Colums(Float, nullable=False)
    longitude = Colums(Float, nullable=False)
