#!/usr/bin/python3
""" Base Unittest Module """
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """ All tests for Base module """
    def test_init_id(self):
        Base._Base__nb_objects = 0
        obj = Base(42)
        self.assertEqual(obj.id, 42)

    def test_init_no_id(self):
        Base._Base__nb_objects = 0
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)

    def test_type(self):
        self.assertEqual(type(Base), type)

    def test_to_json_string(self):
        Base._Base__nb_objects = 0
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")
        self.assertEqual(Base.to_json_string(
            [{'id': 1, 'x': 2, 'y': 3}]), '[{"id": 1, "x": 2, "y": 3}]')

    def test_save_to_file(self):
        Base._Base__nb_objects = 0
        Rec1 = Rectangle(5, 4, 3, 2)
        Rec2 = Rectangle(1, 2)
        Rectangle.save_to_file([Rec1, Rec2])
        with open("Rectangle.json", 'r') as f:
            self.assertEqual(f.read(), '[{"x": 3, "y": 2, "id": 1, \
"height": 4, "width": 5}, {"x": 0, "y": 0, "id": 2, "height": 2, "width": 1}]')

    def test_create(self):
        Base._text__nb_objects = 0
        Dict1 = {"x": 1, "y": 2, "id": 3, "height": 4, "weight": 5}
        Rect1 = Rectangle.create(**Dict1)
        self.assertIsInstance(Rect1, Rectangle)
        self.assertEqual(Rect1.__str__(), "[Rectangle] (3) 1/2 - 5/4")

    def test_load_from_file(self):
        Base._Base__nb_objects = 0
        pass


if __name__ == "__main__":
    unittest.main()
