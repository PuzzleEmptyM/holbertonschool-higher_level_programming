#!/usr/bin/python3
""" rectangle.py unittest definitions """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch
from io import StringIO


class TestRectangle_class(unittest.TestCase):
    """ tests for Rectangle class """
    def setUp(self):
        self.instance = Rectangle(8, 16, 2, 4, 12)

    def test_width_getter(self):
        self.assertEqual(self.instance.width, 8)

    def test_height_getter(self):
        self.assertEqual(self.instance.height, 16)

    def test_x_getter(self):
        self.assertEqual(self.instance.x, 2)

    def test_y_getter(self):
        self.assertEqual(self.instance.y, 4)

    def test_id(self):
        self.assertEqual(self.instance.id, 12)

    def test_setters(self):
        self.instance.width = 12
        self.instance.height = 20
        self.instance.x = 6
        self.instance.y = 8
        self.instance.id = 16
        self.assertEqual(
            [
                self.instance.width,
                self.instance.height,
                self.instance.x,
                self.instance.y,
                self.instance.id
            ],
            [12, 20, 6, 8, 16]
        )

    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_single_argument(self):
        with self.assertRaises(TypeError):
            Rectangle(2)

    def test_excessive_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle(32, 64, 128, 256, 512, 1024, 2048)

    def test_private_width(self):
        with self.assertRaises(AttributeError):
            print(self.instance.__width)

    def test_private_height(self):
        with self.assertRaises(AttributeError):
            print(self.instance.__height)

    def test_private_x(self):
        with self.assertRaises(AttributeError):
            print(self.instance.__x)

    def test_private_y(self):
        with self.assertRaises(AttributeError):
            print(self.instance.__y)

    def test_width_value_exception(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-2, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_width_type_exception(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("surfin", 4)

    def test_height_value_exception(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, -4)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(2, 0)

    def test_height_type_exception(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, "dude")

    def test_x_value_exception(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(2, 4, -8)

    def test_x_type_exception(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(2, 4, "dude")

    def test_y_value_exception(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(2, 4, 8, -16)

    def test_y_type_exception(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(2, 4, 8, "dude")

    def test_type(self):
        self.assertEqual(type(self.instance), Rectangle)
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertIs(Rectangle, Rectangle)

    def test_doc_strings(self):
        self.assertTrue(len(Rectangle.__doc__) >= 1)
        self.assertTrue(len(Rectangle.__init__.__doc__) >= 1)
        self.assertTrue(len(Rectangle.area.__doc__) >= 1)
        self.assertTrue(len(Rectangle.display.__doc__) >= 1)
        self.assertTrue(len(Rectangle.update.__doc__) >= 1)
        self.assertTrue(len(Rectangle.to_dictionary.__doc__) >= 1)
        self.assertTrue(len(Rectangle.__str__.__doc__) >= 1)

    def test_str(self):
        self.assertEqual(str(self.instance), "[Rectangle] (12) 2/4 - 8/16")

    def test_str_with_argument(self):
        with self.assertRaises(TypeError):
            self.instance.__str__(12)


class TestRectangle_setters_invalid_attribute_types(unittest.TestCase):
    """ tests for Rectangle invalid instantiation attributes """
    def setUp(self):
        self.instance = Rectangle(2, 4, 8, 16, 12)

    def test_setter_invalid_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.width = 3.14
            Rectangle(3.14, 4)

    def test_setter_invalid_width_complex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.width = complex(6)
            Rectangle(complex(6), 4)

    def test_setter_invalid_width_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.width = range(6)
            Rectangle(range(6), 4)

    def test_setter_invalid_width_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.width = float('inf')
            Rectangle(float('inf'), 4)

    def test_setter_invalid_width_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.width = float('nan')
            Rectangle(float('nan'), 4)

    def test_setter_invalid_width_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.width = "dude"
            Rectangle("dude", 4)

    def test_setter_invalid_width_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.width = True
            Rectangle(True, 4)

    def test_setter_invalid_width_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.width = None
            Rectangle(None, 4)

    def test_setter_invalid_width_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.width = (2, 4)
            Rectangle((2, 4), 4)

    def test_setter_invalid_width_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.width = [6, 6]
            Rectangle([6, 6], 4)

    def test_setter_invalid_width_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.width = {'width': 6}
            Rectangle({'width': 6}, 4)

    def test_setter_invalid_width_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.width = {3, 6, 9}
            Rectangle({3, 6, 9}, 4)

    def test_setter_invalid_width_frozenset(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.width = frozenset({3, 6, 9})
            Rectangle(frozenset({3, 6, 9}), 4)

    def test_setter_invalid_width_byte(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.width = b'dude'
            Rectangle(b'dude', 4)

    def test_setter_invalid_width_bytearray(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.width = bytearray(b'dude')
            Rectangle(bytearray(b'dude'), 4)

    def test_setter_invalid_width_memoryview(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.width = memoryview(b'dude')
            Rectangle(memoryview(b'dude'), 4)

    def test_setter_invalid_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.height = 3.14
            Rectangle(2, 3.14)

    def test_setter_invalid_height_complex(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.height = complex(6)
            Rectangle(2, complex(6))

    def test_setter_invalid_height_range(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.height = range(6)
            Rectangle(2, range(6))

    def test_setter_invalid_height_inf(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.height = float('inf')
            Rectangle(2, float('inf'))

    def test_setter_invalid_height_nan(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.height = float('nan')
            Rectangle(2, float('nan'))

    def test_setter_invalid_height_string(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.height = "dude"
            Rectangle(2, "dude")

    def test_setter_invalid_height_bool(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.height = True
            Rectangle(2, True)

    def test_setter_invalid_height_none(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.height = None
            Rectangle(2, None)

    def test_setter_invalid_height_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.height = (2, 4)
            Rectangle(2, (2, 4))

    def test_setter_invalid_height_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.height = [6, 6]
            Rectangle(2, [6, 6])

    def test_setter_invalid_height_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.height = {'height': 6}
            Rectangle(2, {'height': 6})

    def test_setter_invalid_height_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.height = {3, 6, 9}
            Rectangle(2, {3, 6, 9})

    def test_setter_invalid_height_frozenset(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.height = frozenset({3, 6, 9})
            Rectangle(2, frozenset({3, 6, 9}))

    def test_setter_invalid_height_byte(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.height = b'dude'
            Rectangle(2, b'dude')

    def test_setter_invalid_height_bytearray(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.height = bytearray(b'dude')
            Rectangle(2, bytearray(b'dude'))

    def test_setter_invalid_height_memoryview(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.height = memoryview(b'dude')
            Rectangle(2, memoryview(b'dude'))

    def test_setter_invalid_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = 3.14
            Rectangle(2, 4, 3.14)

    def test_setter_invalid_x_complex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = complex(6)
            Rectangle(2, 4, complex(6))

    def test_setter_invalid_x_range(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = range(6)
            Rectangle(2, 4, range(6))

    def test_setter_invalid_x_inf(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = float('inf')
            Rectangle(2, 4, float('inf'))

    def test_setter_invalid_x_nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = float('nan')
            Rectangle(2, 4, float('nan'))

    def test_setter_invalid_x_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = "dude"
            Rectangle(2, 4, "dude")

    def test_setter_invalid_x_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = True
            Rectangle(2, 4, True)

    def test_setter_invalid_x_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = None
            Rectangle(2, 4, None)

    def test_setter_invalid_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = (2, 4)
            Rectangle(2, 4, (2, 4))

    def test_setter_invalid_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = [6, 6]
            Rectangle(2, 4, [6, 6])

    def test_setter_invalid_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = {'x': 6}
            Rectangle(2, 4, {'x': 6})

    def test_setter_invalid_x_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = {3, 6, 9}
            Rectangle(2, 4, {3, 6, 9})

    def test_setter_invalid_x_frozenset(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = frozenset({3, 6, 9})
            Rectangle(2, 4, frozenset({3, 6, 9}))

    def test_setter_invalid_x_byte(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = b'dude'
            Rectangle(2, 4, b'dude')

    def test_setter_invalid_x_bytearray(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = bytearray(b'dude')
            Rectangle(2, 4, bytearray(b'dude'))

    def test_setter_invalid_x_memoryview(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = memoryview(b'dude')
            Rectangle(2, 4, memoryview(b'dude'))

    def test_setter_invalid_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = 3.14
            Rectangle(2, 4, 8, 3.14)

    def test_setter_invalid_y_complex(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = complex(6)
            Rectangle(2, 4, 8, complex(6))

    def test_setter_invalid_y_range(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = range(6)
            Rectangle(2, 4, 8, range(6))

    def test_setter_invalid_y_inf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = float('inf')
            Rectangle(2, 4, 8, float('inf'))

    def test_setter_invalid_y_nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = float('nan')
            Rectangle(2, 4, 8, float('nan'))

    def test_setter_invalid_y_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = "dude"
            Rectangle(2, 4, 8, "dude")

    def test_setter_invalid_y_bool(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = True
            Rectangle(2, 4, 8, True)

    def test_setter_invalid_y_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = None
            Rectangle(2, 4, 8, None)

    def test_setter_invalid_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = (2, 4)
            Rectangle(2, 4, 8, (2, 4))

    def test_setter_invalid_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = [6, 6]
            Rectangle(2, 4, 8, [6, 6])

    def test_setter_invalid_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = {'x': 6}
            Rectangle(2, 4, 8, {'x': 6})

    def test_setter_invalid_y_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = {3, 6, 9}
            Rectangle(2, 4, 8, {3, 6, 9})

    def test_setter_invalid_y_frozenset(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = frozenset({3, 6, 9})
            Rectangle(2, 4, 8, frozenset({3, 6, 9}))

    def test_setter_invalid_y_byte(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = b'dude'
            Rectangle(2, 4, 8, b'dude')

    def test_setter_invalid_y_bytearray(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = bytearray(b'dude')
            Rectangle(2, 4, 8, bytearray(b'dude'))

    def test_setter_invalid_y_memoryview(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = memoryview(b'dude')
            Rectangle(2, 4, 8, memoryview(b'dude'))


class TestRectangle_area(unittest.TestCase):
    """ tests for Rectangle area method """
    def setUp(self):
        self.instance = Rectangle(2, 4, 8, 16, 12)

    def test_area(self):
        self.assertEqual(Rectangle(4, 6).area(), 24)

    def test_area_INT_MAX_UINT_MAX(self):
        self.instance.width = 2147483647
        self.instance.height = 4294967295
        self.assertEqual(self.instance.area(), 9223372030412324865)

    def test_area_with_argument(self):
        with self.assertRaises(TypeError):
            self.instance.area(24)


class TestRectangle_display(unittest.TestCase):
    """ tests for Rectangle display method """
    def test_display_rectangle_2w_4h(self):
        with patch('sys.stdout', new=StringIO()) as comp:
            Rectangle(2, 4).display()
            self.assertEqual(
                comp.getvalue(),
                "##\n##\n##\n##\n"
            )

    def test_display_rectangle_as_square_6w_6h(self):
        with patch('sys.stdout', new=StringIO()) as comp:
            Rectangle(6, 6).display()
            self.assertEqual(
                comp.getvalue(),
                "######\n######\n######\n######\n######\n######\n"
            )

    def test_display_rectangle_2w_4h_2x_4y(self):
        with patch('sys.stdout', new=StringIO()) as comp:
            Rectangle(2, 4, 2, 4).display()
            self.assertEqual(
                comp.getvalue(),
                "\n\n\n\n  ##\n  ##\n  ##\n  ##\n"
            )

    def test_display_rectangle_2w_4h_0x_4y(self):
        with patch('sys.stdout', new=StringIO()) as comp:
            Rectangle(2, 4, 0, 4).display()
            self.assertEqual(
                comp.getvalue(),
                "\n\n\n\n##\n##\n##\n##\n"
            )

    def test_display_rectangle_2w_4h_2x_0y(self):
        with patch('sys.stdout', new=StringIO()) as comp:
            Rectangle(2, 4, 2).display()
            self.assertEqual(
                comp.getvalue(),
                "  ##\n  ##\n  ##\n  ##\n"
            )

    def test_display_with_argument(self):
        with self.assertRaises(TypeError):
            Rectangle(2, 4).display(2)


class TestRectangle_update(unittest.TestCase):
    """ tests for Rectangle update method """
    def setUp(self):
        self.instance = Rectangle(2, 4, 8, 16, 12)

    def test_update_id(self):
        self.instance.update(16)
        self.assertEqual(str(self.instance), "[Rectangle] (16) 8/16 - 2/4")

    def test_update_width(self):
        self.instance.update(16, 6)
        self.assertEqual(str(self.instance), "[Rectangle] (16) 8/16 - 6/4")

    def test_update_height(self):
        self.instance.update(16, 6, 10)
        self.assertEqual(str(self.instance), "[Rectangle] (16) 8/16 - 6/10")

    def test_update_x(self):
        self.instance.update(16, 6, 10, 12)
        self.assertEqual(str(self.instance), "[Rectangle] (16) 12/16 - 6/10")

    def test_update_y(self):
        self.instance.update(16, 6, 10, 12, 20)
        self.assertEqual(str(self.instance), "[Rectangle] (16) 12/20 - 6/10")

    def test_update_no_arguments(self):
        self.instance.update()
        self.assertEqual(str(self.instance), "[Rectangle] (12) 8/16 - 2/4")

    def test_update_kwargs_id(self):
        self.instance.update(**{'id': 24})
        self.assertEqual(str(self.instance), "[Rectangle] (24) 8/16 - 2/4")

    def test_update_kwargs_width(self):
        self.instance.update(**{'id': 24, 'width': 4})
        self.assertEqual(str(self.instance), "[Rectangle] (24) 8/16 - 4/4")

    def test_update_kwargs_height(self):
        self.instance.update(**{'id': 24, 'width': 4, 'height': 8})
        self.assertEqual(str(self.instance), "[Rectangle] (24) 8/16 - 4/8")

    def test_update_kwargs_x(self):
        self.instance.update(**{'id': 24, 'width': 4, 'height': 8, 'x': 16})
        self.assertEqual(str(self.instance), "[Rectangle] (24) 16/16 - 4/8")

    def test_update_kwargs_y(self):
        self.instance.update(**{
            'id': 24,
            'width': 4,
            'height': 8,
            'x': 16,
            'y': 32
        })
        self.assertEqual(str(self.instance), "[Rectangle] (24) 16/32 - 4/8")

    def test_update_kwargs_mixed_arguments(self):
        self.instance.update(112, 144, y=66, x=96)
        self.assertEqual(str(self.instance), "[Rectangle] (112) 8/16 - 144/4")

    def test_update_kwargs_no_matches_found(self):
        self.instance.update(dude=100, surf=200)
        self.assertEqual(str(self.instance), "[Rectangle] (12) 8/16 - 2/4")

    def test_update_kwargs_mixmatch(self):
        self.instance.update(dude=100, id=144, surf=200, x=60, y=70)
        self.assertEqual(str(self.instance), "[Rectangle] (144) 60/70 - 2/4")


class TestRectangle_updates_invalid_attribute_types(unittest.TestCase):
    """ tests for Rectangle invalid update method attributes """
    def setUp(self):
        self.instance = Rectangle(2, 4, 8, 16, 12)

    def test_update_invalid_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, 3.14)

    def test_update_invalid_width_complex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, complex(6))

    def test_update_invalid_width_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, range(6))

    def test_update_invalid_width_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, float('inf'))

    def test_update_invalid_width_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, float('nan'))

    def test_update_invalid_width_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, "dude")

    def test_update_invalid_width_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, True)

    def test_update_invalid_width_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, None)

    def test_update_invalid_width_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, (2, 4))

    def test_update_invalid_width_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, [6, 6])

    def test_update_invalid_width_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, {'width': 6})

    def test_update_invalid_width_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, {3, 6, 9})

    def test_update_invalid_width_frozenset(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, frozenset({3, 6, 9}))

    def test_update_invalid_width_byte(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, b'dude')

    def test_update_invalid_width_bytearray(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, bytearray(b'dude'))

    def test_update_invalid_width_memoryview(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, memoryview(b'dude'))

    def test_update_invalid_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                3.14
            )

    def test_update_invalid_height_complex(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                complex(6)
            )

    def test_update_invalid_height_range(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                range(6)
            )

    def test_update_invalid_height_inf(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                float('inf')
            )

    def test_update_invalid_height_nan(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                float('nan')
            )

    def test_update_invalid_height_string(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                "dude"
            )

    def test_update_invalid_height_bool(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                True
            )

    def test_update_invalid_height_none(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                None
            )

    def test_update_invalid_height_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                (2, 4)
            )

    def test_update_invalid_height_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                [6, 6]
            )

    def test_update_invalid_height_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                {'width': 6}
            )

    def test_update_invalid_height_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                {3, 6, 9}
            )

    def test_update_invalid_height_frozenset(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                frozenset({3, 6, 9})
            )

    def test_update_invalid_height_byte(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                b'dude'
            )

    def test_update_invalid_height_bytearray(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                bytearray(b'dude')
            )

    def test_update_invalid_height_memoryview(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                memoryview(b'dude')
            )

    def test_update_invalid_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                3.14
            )

    def test_update_invalid_x_complex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                complex(6)
            )

    def test_update_invalid_x_range(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                range(6)
            )

    def test_update_invalid_x_inf(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                float('inf')
            )

    def test_update_invalid_x_nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                float('nan')
            )

    def test_update_invalid_x_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                "dude"
            )

    def test_update_invalid_x_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                True
            )

    def test_update_invalid_x_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                None
            )

    def test_update_invalid_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                (2, 4)
            )

    def test_update_invalid_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                [6, 6]
            )

    def test_update_invalid_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                {'width': 6}
            )

    def test_update_invalid_x_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                {3, 6, 9}
            )

    def test_update_invalid_x_frozenset(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                frozenset({3, 6, 9})
            )

    def test_update_invalid_x_byte(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                b'dude'
            )

    def test_update_invalid_x_bytearray(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                bytearray(b'dude')
            )

    def test_update_invalid_x_memoryview(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                memoryview(b'dude')
            )

    def test_update_invalid_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                self.instance.x,
                3.14
            )

    def test_update_invalid_y_complex(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                self.instance.x,
                complex(6)
            )

    def test_update_invalid_y_range(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                self.instance.x,
                range(6)
            )

    def test_update_invalid_y_inf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                self.instance.x,
                float('inf')
            )

    def test_update_invalid_y_nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                self.instance.x,
                float('nan')
            )

    def test_update_invalid_y_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                self.instance.x,
                "dude"
            )

    def test_update_invalid_y_bool(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                self.instance.x,
                True
            )

    def test_update_invalid_y_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                self.instance.x,
                None
            )

    def test_update_invalid_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                self.instance.x,
                (2, 4)
            )

    def test_update_invalid_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                self.instance.x,
                [6, 6]
            )

    def test_update_invalid_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                self.instance.x,
                {'width': 6}
            )

    def test_update_invalid_y_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                self.instance.x,
                {3, 6, 9}
            )

    def test_update_invalid_y_frozenset(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                self.instance.x,
                frozenset({3, 6, 9})
            )

    def test_update_invalid_y_byte(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                self.instance.x,
                b'dude'
            )

    def test_update_invalid_y_bytearray(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                self.instance.x,
                bytearray(b'dude')
            )

    def test_update_invalid_y_memoryview(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.width,
                self.instance.height,
                self.instance.x,
                memoryview(b'dude')
            )

    def test_update_kwargs_invalid_width_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(width=3.14)

    def test_update_kwargs_invalid_width_complex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(width=complex(6))

    def test_update_kwargs_invalid_width_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(width=range(6))

    def test_update_kwargs_invalid_width_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(width=float('inf'))

    def test_update_kwargs_invalid_width_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(width=float('nan'))

    def test_update_kwargs_invalid_width_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(width="dude")

    def test_update_kwargs_invalid_width_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(width=True)

    def test_update_kwargs_invalid_width_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(width=None)

    def test_update_kwargs_invalid_width_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(width=(2, 4))

    def test_update_kwargs_invalid_width_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(width=[6, 6])

    def test_update_kwargs_invalid_width_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(width={'width': 6})

    def test_update_kwargs_invalid_width_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(width={3, 6, 9})

    def test_update_kwargs_invalid_width_frozenset(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(width=frozenset({3, 6, 9}))

    def test_update_kwargs_invalid_width_byte(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(width=b'dude')

    def test_update_kwargs_invalid_width_bytearray(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(width=bytearray(b'dude'))

    def test_update_kwargs_invalid_width_memoryview(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(width=memoryview(b'dude'))

    def test_update_kwargs_invalid_height_float(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(height=3.14)

    def test_update_kwargs_invalid_height_complex(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(height=complex(6))

    def test_update_kwargs_invalid_height_range(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(height=range(6))

    def test_update_kwargs_invalid_height_inf(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(height=float('inf'))

    def test_update_kwargs_invalid_height_nan(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(height=float('nan'))

    def test_update_kwargs_invalid_height_string(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(height="dude")

    def test_update_kwargs_invalid_height_bool(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(height=True)

    def test_update_kwargs_invalid_height_none(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(height=None)

    def test_update_kwargs_invalid_height_tuple(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(height=(2, 4))

    def test_update_kwargs_invalid_height_list(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(height=[6, 6])

    def test_update_kwargs_invalid_height_dict(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(height={'width': 6})

    def test_update_kwargs_invalid_height_set(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(height={3, 6, 9})

    def test_update_kwargs_invalid_height_frozenset(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(height=frozenset({3, 6, 9}))

    def test_update_kwargs_invalid_height_byte(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(height=b'dude')

    def test_update_kwargs_invalid_height_bytearray(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(height=bytearray(b'dude'))

    def test_update_kwargs_invalid_height_memoryview(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.instance.update(height=memoryview(b'dude'))

    def test_update_kwargs_invalid_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(x=3.14)

    def test_update_kwargs_invalid_x_complex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(x=complex(6))

    def test_update_kwargs_invalid_x_range(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(x=range(6))

    def test_update_kwargs_invalid_x_inf(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(x=float('inf'))

    def test_update_kwargs_invalid_x_nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(x=float('nan'))

    def test_update_kwargs_invalid_x_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(x="dude")

    def test_update_kwargs_invalid_x_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(x=True)

    def test_update_kwargs_invalid_x_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(x=None)

    def test_update_kwargs_invalid_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(x=(2, 4))

    def test_update_kwargs_invalid_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(x=[6, 6])

    def test_update_kwargs_invalid_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(x={'width': 6})

    def test_update_kwargs_invalid_x_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(x={3, 6, 9})

    def test_update_kwargs_invalid_x_frozenset(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(x=frozenset({3, 6, 9}))

    def test_update_kwargs_invalid_x_byte(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(x=b'dude')

    def test_update_kwargs_invalid_x_bytearray(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(x=bytearray(b'dude'))

    def test_update_kwargs_invalid_x_memoryview(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(x=memoryview(b'dude'))

    def test_update_kwargs_invalid_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(y=3.14)

    def test_update_kwargs_invalid_y_complex(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(y=complex(6))

    def test_update_kwargs_invalid_y_range(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(y=range(6))

    def test_update_kwargs_invalid_y_inf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(y=float('inf'))

    def test_update_kwargs_invalid_y_nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(y=float('nan'))

    def test_update_kwargs_invalid_y_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(y="dude")

    def test_update_kwargs_invalid_y_bool(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(y=True)

    def test_update_kwargs_invalid_y_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(y=None)

    def test_update_kwargs_invalid_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(y=(2, 4))

    def test_update_kwargs_invalid_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(y=[6, 6])

    def test_update_kwargs_invalid_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(y={'width': 6})

    def test_update_kwargs_invalid_y_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(y={3, 6, 9})

    def test_update_kwargs_invalid_y_frozenset(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(y=frozenset({3, 6, 9}))

    def test_update_kwargs_invalid_y_byte(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(y=b'dude')

    def test_update_kwargs_invalid_y_bytearray(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(y=bytearray(b'dude'))

    def test_update_kwargs_invalid_y_memoryview(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(y=memoryview(b'dude'))


class TestRectangle_to_dictionary(unittest.TestCase):
    """ tests for Rectangle to_dictionary method """
    def setUp(self):
        self.instance = Rectangle(2, 4, 8, 16, 12)
        self.inst_dict = {'id': 12, 'width': 2, 'height': 4, 'x': 8, 'y': 16}

    def test_to_dictionary(self):
        self.assertDictEqual(self.instance.to_dictionary(), self.inst_dict)

    def test_to_dictionary_update_kwargs(self):
        rect_inst = Rectangle(20, 40, 80, 160, 120)
        rect_inst.update(**self.instance.to_dictionary())
        self.assertNotEqual(hex(id(self.instance)), hex(id(rect_inst)))

    def test_to_dictionary_with_argument(self):
        with self.assertRaises(TypeError):
            self.instance.to_dictionary(12)


if __name__ == "__main__":
    unittest.main()
