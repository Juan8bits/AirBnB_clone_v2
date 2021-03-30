#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float, ForeignKey, MetaData
from sqlalchemy import Table
from sqlalchemy.orm import relationship
import os

place_amenity = Table('place_amenity', Base.metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False)
                      )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship('Review', backref='place',
                               cascade='all, delete')
        amenities = relationship("Amenity", secondary=place_amenity,
                                 backref="place", viewonly=False)
    else:
        @property
        def reviews(self):
            """Getter reviews"""
            reviews = models.storage.all(City)
            list_reviews = []
            for i in reviews.values():
                if self.id == i.state_id:
                    list_reviews.append(i)
            return list_reviews

        @property
        def amenities(self):
            """Getter for amenities with FileStorage engine"""
            amenities = models.sotrage.all(Amenity)
            list_amenity = []
            for i in amenities.values():
                if self.id == i.amenity_ids:
                    list_amenity.append(i)
            return list_amenity

        @amenities.setter
        def amenities(self, value):
            """ Setter for amenities method"""
            if type(value) is Amenity:
                amenities.append(value)
