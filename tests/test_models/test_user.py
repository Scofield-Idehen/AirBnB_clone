#!/usr/bin/python3
"""Unit test User"""
import unittest
import models
from models.user import User
import os


class TestUser(unittest.TestCase):
    """Test for class User"""

    def test_user_attributes(self):
        """Test for attributes present in class User"""
        user = User()
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_user_initial_attributes(self):
        """Test for initial attributes in class User"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_attribute_assignment(self):
        """Test for attribute assignment in class User"""
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_id(self):
        """Test that id is unique"""
        my_objectId = User()
        my_objectId1 = User()
        self.assertNotEqual(my_objectId.id, my_objectId1.id)

    def test_docstring(self):
        """Test if functions, methods, classes, and modules have docstring"""
        message = "Modules does not have docstring"
        self.assertIsNotNone(models.user.__doc__, message)
        message2 = "Classes does not have docstring"
        self.assertIsNotNone(User.__doc__, message2)

    def test_executable_file(self):
        """Test if file has permissions to read, write, and execute"""
        is_read_true = os.access('models/user.py', os.R_OK)
        self.assertTrue(is_read_true)

        is_write_true = os.access('models/user.py', os.W_OK)
        self.assertTrue(is_write_true)


if __name__ == '__main__':
    unittest.main()
