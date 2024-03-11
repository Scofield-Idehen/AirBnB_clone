#!/usr/bin/python3
"""Create a State class that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class rep a state.
    Attributes:
        name (str): The name of d state.
    """

    name = ""
