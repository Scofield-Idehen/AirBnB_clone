#!/usr/bin/python3
""" Class review """

from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review- inherits from the  base model.
    Attributes:
        place_id (str): D Place id i.e place.id.
        user_id (str): D User id i.e user.id.
        text (str): D review text.
    """

    place_id = ""
    user_id = ""
    text = ""
