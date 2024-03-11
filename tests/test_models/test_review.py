import unittest
from models.review import Review
import models
from datetime import datetime
from time import sleep


class TestReview(unittest.TestCase):
    """Test cases for Review class"""

    def test_no_args(self):
        """Test for no arguments"""
        self.assertEqual(Review, type(Review()))

    def test_new_instance_stored(self):
        """Test cases for new instances stored in obj"""
        self.assertIn(Review(), models.storage.all().values())

    def test_id_is_str(self):
        """Test if id is string"""
        self.assertEqual(str, type(Review().id))

    def test_created_at_is_datetime(self):
        """Test if createdAt is datetime"""
        self.assertEqual(datetime, type(Review().created_at))

    def test_updated_at_is_datetime(self):
        """Test if updatedAt is datetime"""
        self.assertEqual(datetime, type(Review().updated_at))

    def test_review_attributes(self):
        """Test the attributes present in the Review class"""
        review = Review()
        self.assertTrue(hasattr(review, 'id'))
        self.assertTrue(hasattr(review, 'created_at'))
        self.assertTrue(hasattr(review, 'updated_at'))
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_review_initial_attributes(self):
        """Test the initial attribute values in the Review class"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_attribute_assignment(self):
        """Test attribute assignment in the Review class"""
        review = Review()
        review.place_id = "12345"
        review.user_id = "67890"
        review.text = "Great place to stay!"

        self.assertEqual(review.place_id, "12345")
        self.assertEqual(review.user_id, "67890")
        self.assertEqual(review.text, "Great place to stay!")

    def test_one_save(self):
        """Test for one save"""
        review = Review()
        sleep(0.05)
        first_updated_at = review.updated_at
        review.save()
        self.assertLess(first_updated_at, review.updated_at)

    def test_two_saves(self):
        """Test for two saves"""
        review = Review()
        sleep(0.05)
        first_updated_at = review.updated_at
        review.save()
        second_updated_at = review.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        review.save()
        self.assertLess(second_updated_at, review.updated_at)

    def test_save_with_arg(self):
        """Test for save with args"""
        review = Review()
        with self.assertRaises(TypeError):
            review.save(None)

    def test_save_updates_file(self):
        """Test for updated file"""
        review = Review()
        review.save()
        revid = "Review." + review.id
        with open("file.json", "r") as f:
            self.assertIn(revid, f.read())


if __name__ == '__main__':
    unittest.main()
