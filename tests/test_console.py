import unittest
import models
import os
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Unittests for testing prompting of the HBNB command interpreter."""

    def setUp(self):
        """Setup method"""
        self.console = HBNBCommand()

    def tearDown(self):
        """Teardown method"""
        pass

    def test_prompt_string(self):
        """Test prompt output"""
        self.assertEqual("(hbnb) ", HBNBCommand.prompt)

    @patch('sys.stdout', new_callable=StringIO)
    def test_quit_command(self, mock_stdout):
        self.console.do_quit("")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_eof_command(self, mock_stdout):
        self.assertTrue(self.console.do_EOF(""))
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline_command(self, mock_stdout):
        self.console.emptyline()
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "")

    def test_create_missing_class(self):
        """Test when class is missing"""
        error_msg = "** class name missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create"))
            self.assertEqual(error_msg, output.getvalue().strip())

    def test_create_invalid_class(self):
        """Test when class name is not in the list."""
        error_msg = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create MyModel"))
            self.assertEqual(error_msg, output.getvalue().strip())

    def test_create_invalid_syntax(self):
        """Test wrong syntax."""
        correct = "*** Unknown syntax: MyModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.create()"))
            self.assertEqual(correct, output.getvalue().strip())
        correct = "*** Unknown syntax: BaseModel.create()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.create()"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_show_missing_class(self):
        """Test show with missing class"""
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("show"))
            self.assertEqual("** class name missing **",
                             output.getvalue().strip())

    def test_show_invalid_class(self):
        """Test show with invalid class"""
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("show MyModel"))
            self.assertEqual("** class doesn't exist **",
                             output.getvalue().strip())

    def test_destroy_id_missing_space_notation(self):
        """Test destroy with missing id"""
        correct = "** instance id missing **"
        classes = ['BaseModel', 'User', 'State',
                   'City', 'Amenity', 'Place', 'Review']
        for class_name in classes:
            with patch("sys.stdout", new_callable=StringIO) as output:
                self.assertFalse(HBNBCommand().onecmd(f"destroy {class_name}"))
                self.assertEqual(correct, output.getvalue().strip())

    def test_all_invalid_class(self):
        """Test all with invalid class"""
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_class(self):
        """Test update with missing class"""
        correct = "** class name missing **"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("update"))
            self.assertEqual(correct, output.getvalue().strip())

        correct2 = "** instance id missing **"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("update ."))
            self.assertEqual(correct2, output.getvalue().strip())

    def test_update_invalid_class(self):
        """Test update with invalid class"""
        correct = "** instance id missing **"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("update MyModel"))
            self.assertEqual(correct, output.getvalue().strip())

    def test_update_missing_id(self):
        """Test update with missing id"""
        correct = "** instance id missing **"
        classes = ['BaseModel', 'User', 'State',
                   'City', 'Amenity', 'Place', 'Review']
        for class_name in classes:
            with patch("sys.stdout", new_callable=StringIO) as output:
                self.assertFalse(HBNBCommand().onecmd(f"update {class_name}"))
                self.assertEqual(correct, output.getvalue().strip())

    @patch('sys.stdout', new_callable=StringIO)
    def test_count_class_not_exist(self, mock_stdout):
        """Test count command when class doesn't exist"""
        HBNBCommand().onecmd("count WrongClass")
        output = mock_stdout.getvalue().strip()
        self.assertEqual("** class doesn't exist **", output)


class TestHBNBCommand_help(unittest.TestCase):
    """Unittests for testing help messages."""

    def test_help(self):
        help_text = (
            "Documented commands (type help <topic>):\n"
            "========================================\n"
            "EOF  all  count  create  destroy  help  quit  show  update"
        )
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("help"))
            self.assertEqual(help_text, output.getvalue().strip())

    def test_help_quit(self):
        help_text = "Quit command to exit the program"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("help quit"))
            self.assertEqual(help_text, output.getvalue().strip())

    def test_help_EOF(self):
        help_text = "Signal to exit the program"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("help EOF"))
            self.assertEqual(help_text, output.getvalue().strip())

    def test_help_create(self):
        help_text = "Create a new class instance and print its id"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("help create"))
            self.assertEqual(help_text, output.getvalue().strip())

    def test_help_show(self):
        help_text = "Prints the str rep of an inst based on class name and id"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("help show"))
            self.assertEqual(help_text, output.getvalue().strip())

    def test_help_destroy(self):
        help_text = "Method to delete instance with class and id"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("help destroy"))
            self.assertEqual(help_text, output.getvalue().strip())

    def test_help_all(self):
        help_text = "Prints all string representation of all instances"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("help all"))
            self.assertEqual(help_text, output.getvalue().strip())

    def test_help_update(self):
        help_text = "Updates an instance based on the class name and id"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("help update"))
            self.assertEqual(help_text, output.getvalue().strip())

    def test_help_count(self):
        """Test the help message for count command"""
        help_text = "Retrieve the number of instances of a class"
        with patch("sys.stdout", new_callable=StringIO) as output:
            self.assertFalse(HBNBCommand().onecmd("help count"))
            self.assertEqual(help_text, output.getvalue().strip())

class TestHBNBCommand_all(unittest.TestCase):
    """Unittests for testing all of the HBNB command interpreter."""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        FileStorage.__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_all_invalid_class(self):
        correct = "** class doesn't exist **"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all MyModel"))
            self.assertEqual(correct, output.getvalue().strip())
        correct2 = "*** Unknown syntax: MyModel.all()"
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("MyModel.all()"))
            self.assertEqual(correct2, output.getvalue().strip())

    def test_all_objects_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertIn("User", output.getvalue().strip())
            self.assertIn("State", output.getvalue().strip())
            self.assertIn("Place", output.getvalue().strip())
            self.assertIn("City", output.getvalue().strip())
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertIn("Review", output.getvalue().strip())

    def test_all_objects_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))


    def test_all_single_object_space_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all BaseModel"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all User"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all State"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all City"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Amenity"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Place"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("all Review"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

    def test_all_single_object_dot_notation(self):
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("create BaseModel"))
            self.assertFalse(HBNBCommand().onecmd("create User"))
            self.assertFalse(HBNBCommand().onecmd("create State"))
            self.assertFalse(HBNBCommand().onecmd("create Place"))
            self.assertFalse(HBNBCommand().onecmd("create City"))
            self.assertFalse(HBNBCommand().onecmd("create Amenity"))
            self.assertFalse(HBNBCommand().onecmd("create Review"))
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("BaseModel.all()"))
            self.assertIn("BaseModel", output.getvalue().strip())
            self.assertNotIn("User", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("User.all()"))
            self.assertIn("User", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("State.all()"))
            self.assertIn("State", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("City.all()"))
            self.assertIn("City", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Amenity.all()"))
            self.assertIn("Amenity", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Place.all()"))
            self.assertIn("Place", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertFalse(HBNBCommand().onecmd("Review.all()"))
            self.assertIn("Review", output.getvalue().strip())
            self.assertNotIn("BaseModel", output.getvalue().strip())

if __name__ == '__main__':
    unittest.main()
