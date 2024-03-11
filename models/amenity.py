#!/usr/bin/python3
"""Creates the Amenity class - inherits from BaseModel."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Rep an amenity.
    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
