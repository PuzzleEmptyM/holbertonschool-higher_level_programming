#!/usr/bin/python3
""" Square Unittest Module """
import unittest
from models.base import Base
from models.square import Square


def setUp(self):
    Base._Base__nb_objects = 0


class TestSquare(unittest.TestCase):
    """ All tests for Square module """
    def test_new_square(self):
        s = Square(5, 4, 3, 2)
        self.assertEqual(s.size, 5)
        self.assertEqual(s.x, 4)
        self.assertEqual(s.y, 3)
        self.assertEqual(s.id, 2)

    def test_new_square_1_input(self):
        s = Square(4)
        self.assertEqual(s.size, 4)
        self.assertEqual(s.id, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_new_square_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square('string')
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 2, 'three')

    def test_size_width_height(self):
        s = Square(444)
        self.assertEqual(s.size, 444)
        self.assertEqual(s.width, 444)
        self.assertEqual(s.height, 444)

    def test_update_one_by_one(self):
        s = Square(1)
        s.update(10)
        self.assertEqual(s.id, 10)
        s.update(10, 5)
        self.assertEqual(s.size, 5)
        s.update(10, 5, 4)
        self.assertEqual(s.x, 4)
        s.update(10, 5, 4, 3)
        self.assertEqual(s.y, 3)

    def test_to_dictionary(self):
        s = Square(2, 4, 6, 101)
        expected_dict = {'id': 101, 'size': 2, 'x': 4, 'y': 6}
        self.assertDictEqual(s.to_dictionary(), expected_dict)


if __name__ == "__main__":
    unittest.main()
