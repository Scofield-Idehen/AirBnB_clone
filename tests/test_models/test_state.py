import unittest
from models.state import State
from time import sleep


class TestState(unittest.TestCase):
    def test_state_attributes(self):
        """Test for attributes present in the State class"""
        state = State()
        self.assertTrue(hasattr(state, 'id'))
        self.assertTrue(hasattr(state, 'created_at'))
        self.assertTrue(hasattr(state, 'updated_at'))
        self.assertTrue(hasattr(state, 'name'))

    def test_state_initial_attributes(self):
        """Test for initial attributes in the State class"""
        state = State()
        self.assertEqual(state.name, "")

    def test_state_attribute_assignment(self):
        """Test for attribute assignment in the State class"""
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")

    def test_one_save(self):
        state = State()
        sleep(0.05)
        first_updated_at = state.updated_at
        state.save()
        self.assertLess(first_updated_at, state.updated_at)

    def test_args_unused(self):
        """Test for unused args"""
        state = State(None)
        self.assertNotIn(None, state.__dict__.values())

    def test_state_to_dict(self):
        """Test the to_dict method of the State class"""
        state = State()
        state.name = "California"
        state_dict = state.to_dict()
        self.assertEqual(state_dict['name'], "California")
        self.assertEqual(state_dict['__class__'], "State")

    def test_state_str_representation(self):
        """Test the __str__ method of the State class"""
        state = State()
        state.name = "California"
        str_repr = str(state)
        self.assertTrue("[State]" in str_repr)
        self.assertTrue(state.id in str_repr)
        self.assertTrue(state.name in str_repr)


if __name__ == '__main__':
    unittest.main()
