import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    def test_city_attributes(self):
        """Test the attributes present in the City class"""
        city = City()
        self.assertTrue(hasattr(city, 'id'))
        self.assertTrue(hasattr(city, 'created_at'))
        self.assertTrue(hasattr(city, 'updated_at'))
        self.assertTrue(hasattr(city, 'state_id'))
        self.assertTrue(hasattr(city, 'name'))

    def test_city_initial_attributes(self):
        """Test the initial attribute values in the City class"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_no_args_instantiates(self):
        """test no arg"""
        self.assertEqual(City, type(City()))

    def test_id_is_string(self):
        """test id is public string"""
        self.assertEqual(str, type(City().id))

    def test_created_at_is_datetime(self):
        """test created public datetime"""
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_is_datetime(self):
        """test updated public datetime"""
        self.assertEqual(datetime, type(City().updated_at))

    def test_city_attr_assignment(self):
        """Test attribute assignment in the City class"""
        city = City()
        city.state_id = "state_1"
        city.name = "City A"

        self.assertEqual(city.state_id, "state_1")
        self.assertEqual(city.name, "City A")

    def test_city_str_representation(self):
        """Test the __str__ method of the City class"""
        city = City()
        city.state_id = "state_1"
        city.name = "City A"

        str_repr = str(city)
        self.assertTrue("[City]" in str_repr)
        self.assertTrue(city.id in str_repr)
        self.assertTrue(city.state_id in str_repr)
        self.assertTrue(city.name in str_repr)

    def test_city_to_dict(self):
        """Test the to_dict method of the City class"""
        city = City()
        city.state_id = "state_1"
        city.name = "City A"

        city_dict = city.to_dict()

        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['state_id'], 'state_1')
        self.assertEqual(city_dict['name'], 'City A')
        self.assertTrue('__class__' not in city.__dict__)


if __name__ == '__main__':
    unittest.main()
