import unittest
from models.place import Place
import models
from datetime import datetime
from time import sleep


class TestPlace(unittest.TestCase):
    """Test cases for Place class"""

    def test_no_args(self):
        """Test for no arguments"""
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored(self):
        """Test cases for new instances stored in obj"""
        self.assertIn(Place(), models.storage.all().values())

    def test_id_is_str(self):
        """Test if id is string"""
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_datetime(self):
        """Test if createdAt is datetime"""
        self.assertEqual(datetime, type(Place().created_at))

    def test_updated_at_is_datetime(self):
        """Test if updatedAt is datetime"""
        self.assertEqual(datetime, type(Place().updated_at))

    def test_place_attributes(self):
        """Test the attributes present in the Place class"""
        place = Place()
        self.assertTrue(hasattr(place, 'id'))
        self.assertTrue(hasattr(place, 'created_at'))
        self.assertTrue(hasattr(place, 'updated_at'))
        self.assertTrue(hasattr(place, 'city_id'))
        self.assertTrue(hasattr(place, 'user_id'))
        self.assertTrue(hasattr(place, 'name'))
        self.assertTrue(hasattr(place, 'description'))
        self.assertTrue(hasattr(place, 'number_rooms'))
        self.assertTrue(hasattr(place, 'number_bathrooms'))
        self.assertTrue(hasattr(place, 'max_guest'))
        self.assertTrue(hasattr(place, 'price_by_night'))
        self.assertTrue(hasattr(place, 'latitude'))
        self.assertTrue(hasattr(place, 'longitude'))
        self.assertTrue(hasattr(place, 'amenity_ids'))

    def test_place_initial_attributes(self):
        """Test the initial attribute values in the Place class"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_attribute_assignment(self):
        """Test attribute assignment in the Place class"""
        place = Place()
        place.city_id = "12345"
        place.user_id = "67890"
        place.name = "Cozy House"
        place.description = "A beautiful cozy house"
        place.number_rooms = 3
        place.number_bathrooms = 2
        place.max_guest = 6
        place.price_by_night = 100
        place.latitude = 37.7749
        place.longitude = -122.4194
        place.amenity_ids = ["amenity1", "amenity2"]

        self.assertEqual(place.city_id, "12345")
        self.assertEqual(place.user_id, "67890")
        self.assertEqual(place.name, "Cozy House")
        self.assertEqual(place.description, "A beautiful cozy house")
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 6)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 37.7749)
        self.assertEqual(place.longitude, -122.4194)
        self.assertEqual(place.amenity_ids, ["amenity1", "amenity2"])

    def test_one_save(self):
        """Test for one save"""
        place = Place()
        sleep(0.05)
        first_updated_at = place.updated_at
        place.save()
        self.assertLess(first_updated_at, place.updated_at)

    def test_two_saves(self):
        """Test for two saves"""
        place = Place()
        sleep(0.05)
        first_updated_at = place.updated_at
        place.save()
        second_updated_at = place.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        place.save()
        self.assertLess(second_updated_at, place.updated_at)

    def test_save_with_arg(self):
        """Test for save with args"""
        place = Place()
        with self.assertRaises(TypeError):
            place.save(None)

    def test_save_updates_file(self):
        """Test for updated file"""
        place = Place()
        place.save()
        plid = "Place." + place.id
        with open("file.json", "r") as f:
            self.assertIn(plid, f.read())


if __name__ == '__main__':
    unittest.main()
