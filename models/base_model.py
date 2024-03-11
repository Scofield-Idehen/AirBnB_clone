#!/usr/bin/python3
"""Imported modules for BaseModel class"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """The BaseModel class of HBnB project"""

    def __init__(self, *args, **kwargs):
        """Constructor method for BaseModel class
        Args:
            *args (any): positional arguments
            **kwargs (dict): Key/value pairs of public instance attributes
        """
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(value, timeformat)
                else:
                    self.__dict__[key] = value
        else:
            models.storage.new(self)

    def __str__(self):
        """Returns the string rep  the BaseModel instance"""
        clsname = self.__class__.__name__
        return "[{}] ({}) {}".format(clsname, self.id, self.__dict__)

    def save(self):
        """Updates public instance attr updated_at with current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Returns dictionary containing all keys/values
        """
        dict_duplicate = self.__dict__.copy()
        dict_duplicate["created_at"] = self.created_at.isoformat()
        dict_duplicate["updated_at"] = self.updated_at.isoformat()
        dict_duplicate["__class__"] = self.__class__.__name__
        return dict_duplicate
