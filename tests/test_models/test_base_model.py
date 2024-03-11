#!/usr/bin/python3
""" Unittest for BaseModel Class """

import unittest
import models
import os
from datetime import datetime
import time
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """ Test for BaseModel class"""

    def test_init_BaseModel(self):
        """test if an object is an type BaseModel"""
        my_object = BaseModel()
        self.assertIsInstance(my_object, BaseModel)

    def test_init_without_arguments(self):
        """Test init with arguments"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_init_with_keyword_arguments(self):
        """Test init without arguments"""
        kwargs = {
            "name": "Test Base Model",
            "value": 10,
            "created_at": "2023-01-01T10:00:00.000000",
            "updated_at": "2023-01-01T12:00:00.000000"
        }
        model = BaseModel(**kwargs)
        self.assertEqual(model.name, "Test Base Model")
        self.assertEqual(model.value, 10)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_docstring_presence_module(self):
        """Test if the module has a docstring"""
        self.assertIsNotNone(models.base_model.__doc__,
                             "Module does not have a docstring")

    def test_docstring_presence_class(self):
        """Test if the class has a docstring"""
        self.assertIsNotNone(BaseModel.__doc__,
                             "Class does not have a docstring")

    def test_executable_file(self):
        """test if file has permissions read, write and execution"""
        is_readable = os.access('models/base_model.py', os.R_OK)
        self.assertTrue(is_readable)
        is_writable = os.access('models/base_model.py', os.W_OK)
        self.assertTrue(is_writable)

    def test_unique_id(self):
        """ test if id is unique """
        my_object1 = BaseModel()
        my_object2 = BaseModel()
        self.assertNotEqual(my_object1.id, my_object2.id)

    def test_str(self):
        """check if the output of str is in the specified format"""
        model = BaseModel()
        expected_str = "[BaseModel] ({}) {}".format(model.id, model.__dict__)
        self.assertEqual(str(model), expected_str)

    def test_save(self):
        """ check if date is updated when save """
        my_object = BaseModel()
        first_updated = my_object.updated_at
        # Introduce a delay of 2 seconds using time.sleep()
        time.sleep(2)
        my_object.save()
        updated_after_save = my_object.updated_at
        self.assertNotEqual(first_updated, updated_after_save)

    def test_to_dict(self):
        """check if to_dict returns a dictionary"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn("id", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertIn("__class__", model_dict)


if __name__ == '__main__':
    unittest.main()
