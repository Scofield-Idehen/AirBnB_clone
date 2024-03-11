#!/usr/bin/python3
""" Class City """
from models.base_model import BaseModel


class City(BaseModel):
    """ City class that inherits from BaseModel
    Attributes:
    id(str): ID of the city obj
    name (str): The name of the city
    """
    state_id = ""
    name = ""
