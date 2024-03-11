#!/usr/bin/python3
"""Creates the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Class dat serializes instances to a JSON file
    and deserializes JSON file to instance.

    Attributes:
        __file_path (str): string - path to the JSON file
        __objects (dict): dict - store all obj by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Getter func, returns the dict __objects- retrieve"""
        return FileStorage.__objects

    def new(self, obj):
        """Setter fn, set in __obj with key <obj_class_name>.id -create"""
        """save obj in file in format, BaseModel.<id>:<>"""
        object_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(object_name, obj.id)] = obj

    def save(self):
        """Serialize __objects and save to the JSON file __file_path.
        Use the keys to get the obj in the file - update
        """
        file_object = FileStorage.__objects
        objdict = {obj: file_object[obj].to_dict()
                   for obj in file_object.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(objdict, file)

    def reload(self):
        """Deserialize the JSON file __file_path to __object"""

        """and read if it exists else rtn error - get all and del class key"""
        try:
            with open(FileStorage.__file_path) as file:
                objdict = json.load(file)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
