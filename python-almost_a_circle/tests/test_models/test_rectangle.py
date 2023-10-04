#!/usr/bin/python3
""" Rectangle Unittest Module """

import unittest
from models.base import Base
from models.rectangle import Rectangle


def setUp(self):
    Base._Base__nb_objects = 0


class TestRectangle(unittest.TestCase):
    """ All tests for Rectangle module """
    def test_new_rectangle(self):
        r = Rectangle(4, 8)
        self.assertEqual(r.width, 4)
        self.assertEqual(r.height, 8)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertIsNotNone(r.id)

    def test_type(self):
        self.assertEqual(type(Rectangle), type)

    def test_bad_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle('string', 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(None, 3)

    def test_bad_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(5, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(3, 0)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(10, 'string')
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(3, None)

    def test_bad_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(3, 2, -1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(3, 2, 'string')

    def test_bad_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(3, 2, 1, -1)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(3, 2, 1, 'string')

    def test_area(self):
        r = Rectangle(3, 5)
        self.assertEqual(r.area(), 15)
        r = Rectangle(100, 100)
        self.assertEqual(r.area(), 10000)

    def test_new_rectangle_kwargs(self):
        Base._Base__nb_objects = 0
        r = Rectangle(id=732, width=1, height=2, x=3, y=4)
        self.assertEqual(r.id, 732)
        self.assertEqual(r.width, 1)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_to_dictionary(self):
        r = Rectangle(4, 3, 2, 1)
        self.assertEqual(r.to_dictionary(), {
                        'id': 1, 'width': 4, 'height': 3, 'x': 2, 'y': 1})

    def test_update(self):
        r = Rectangle(6, 8)
        list1 = [1, 2, 3, 4, 5]
        r.update(*list1)
        self.assertEqual(r.width, 2)
        self.assertEqual(r.height, 3)
        self.assertEqual(r.id, 1)
        self.assertEqual(r.x, 4)
        self.assertEqual(r.y, 5)

    def test_update_with_string(self):
        r = Rectangle(6, 8)
        list1 = [1, 2, 3, 4, 'five']
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(*list1)

    def test_update_with_neg(self):
        r = Rectangle(6, 8)
        list1 = [1, 2, -3, 4]
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(*list1)

    def test_to_dictionary(self):
        r = Rectangle(100, 200, 10, 20)
        self.assertEqual(
            r.to_dictionary(),
            {'x': 10, 'y': 20, 'id': 1, 'height': 200, 'width': 100}
        )


if __name__ == "__main__":
    unittest.main()
