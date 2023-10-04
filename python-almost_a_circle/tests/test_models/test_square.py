#!/usr/bin/python3
""" square.py unittest definitions """
import unittest
from models.rectangle import Rectangle
from models.square import Square
from unittest.mock import patch
from io import StringIO


class TestSquare_class(unittest.TestCase):
    """ tests for Square class """
    def setUp(self):
        self.instance = Square(8, 2, 4, 12)

    def test_size_getter(self):
        self.assertEqual(self.instance.size, 8)

    def test_x_getter(self):
        self.assertEqual(self.instance.x, 2)

    def test_y_getter(self):
        self.assertEqual(self.instance.y, 4)

    def test_id(self):
        self.assertEqual(self.instance.id, 12)

    def test_setters(self):
        self.instance.size = 12
        self.instance.x = 20
        self.instance.y = 6
        self.instance.id = 16
        self.assertEqual(
            [
                self.instance.size,
                self.instance.x,
                self.instance.y,
                self.instance.id
            ],
            [12, 20, 6, 16]
        )

    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            Square()

    def test_excessive_arguments(self):
        with self.assertRaises(TypeError):
            Square(32, 64, 128, 256, 512, 1024, 2048)

    def test_private_size(self):
        with self.assertRaises(AttributeError):
            print(self.instance.__size)

    def test_private_x(self):
        with self.assertRaises(AttributeError):
            print(self.instance.__x)

    def test_private_y(self):
        with self.assertRaises(AttributeError):
            print(self.instance.__y)

    def test_width_value_exception(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-2, 4)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)

    def test_width_type_exception(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("surfin", 4)

    def test_x_value_exception(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(2, -4)

    def test_x_type_exception(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(2, "dude")

    def test_y_value_exception(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(2, 4, -8)

    def test_y_type_exception(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(2, 4, "dude")

    def test_type(self):
        self.assertEqual(type(self.instance), Square)
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertIs(Square, Square)

    def test_doc_strings(self):
        self.assertTrue(len(Square.__doc__) >= 1)
        self.assertTrue(len(Square.__init__.__doc__) >= 1)
        self.assertTrue(len(Square.area.__doc__) >= 1)
        self.assertTrue(len(Square.update.__doc__) >= 1)
        self.assertTrue(len(Square.to_dictionary.__doc__) >= 1)
        self.assertTrue(len(Square.__str__.__doc__) >= 1)

    def test_str(self):
        self.assertEqual(str(self.instance), "[Square] (12) 2/4 - 8")

    def test_str_with_argument(self):
        with self.assertRaises(TypeError):
            self.instance.__str__(12)


class TestSquare_setters_invalid_attribute_types(unittest.TestCase):
    """ tests for Square invalid instantiation attributes """
    def setUp(self):
        self.instance = Square(2, 4, 8, 12)

    def test_setter_invalid_size_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.size = 3.14
            Square(3.14)

    def test_setter_invalid_size_complex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.size = complex(6)
            Square(complex(6))

    def test_setter_invalid_size_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.size = range(6)
            Square(range(6))

    def test_setter_invalid_size_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.size = float('inf')
            Square(float('inf'))

    def test_setter_invalid_size_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.size = float('nan')
            Square(float('nan'))

    def test_setter_invalid_size_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.size = "dude"
            Square("dude")

    def test_setter_invalid_size_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.size = True
            Square(True)

    def test_setter_invalid_size_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.size = None
            Square(None)

    def test_setter_invalid_size_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.size = (2, 4)
            Square((2, 4))

    def test_setter_invalid_size_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.size = [6, 6]
            Square([6, 6])

    def test_setter_invalid_size_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.size = {'width': 6}
            Square({'width': 6})

    def test_setter_invalid_size_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.size = {3, 6, 9}
            Square({3, 6, 9})

    def test_setter_invalid_size_frozenset(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.size = frozenset({3, 6, 9})
            Square(frozenset({3, 6, 9}))

    def test_setter_invalid_size_byte(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.size = b'dude'
            Square(b'dude')

    def test_setter_invalid_size_bytearray(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.size = bytearray(b'dude')
            Square(bytearray(b'dude'))

    def test_setter_invalid_size_memoryview(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.size = memoryview(b'dude')
            Square(memoryview(b'dude'))

    def test_setter_invalid_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = 3.14
            Square(2, 3.14)

    def test_setter_invalid_x_complex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = complex(6)
            Square(2, complex(6))

    def test_setter_invalid_x_range(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = range(6)
            Square(2, range(6))

    def test_setter_invalid_x_inf(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = float('inf')
            Square(2, float('inf'))

    def test_setter_invalid_x_nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = float('nan')
            Square(2, float('nan'))

    def test_setter_invalid_x_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = "dude"
            Square(2, "dude")

    def test_setter_invalid_x_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = True
            Square(2, True)

    def test_setter_invalid_x_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = None
            Square(2, None)

    def test_setter_invalid_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = (2, 4)
            Square(2, (2, 4))

    def test_setter_invalid_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = [6, 6]
            Square(2, [6, 6])

    def test_setter_invalid_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = {'x': 6}
            Square(2, {'x': 6})

    def test_setter_invalid_x_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = {3, 6, 9}
            Square(2, {3, 6, 9})

    def test_setter_invalid_x_frozenset(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = frozenset({3, 6, 9})
            Square(2, frozenset({3, 6, 9}))

    def test_setter_invalid_x_byte(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = b'dude'
            Square(2, b'dude')

    def test_setter_invalid_x_bytearray(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = bytearray(b'dude')
            Square(2, bytearray(b'dude'))

    def test_setter_invalid_x_memoryview(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.x = memoryview(b'dude')
            Square(2, memoryview(b'dude'))

    def test_setter_invalid_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = 3.14
            Square(2, 4, 3.14)

    def test_setter_invalid_y_complex(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = complex(6)
            Square(2, 4, complex(6))

    def test_setter_invalid_y_range(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = range(6)
            Square(2, 4, range(6))

    def test_setter_invalid_y_inf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = float('inf')
            Square(2, 4, float('inf'))

    def test_setter_invalid_y_nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = float('nan')
            Square(2, 4, float('nan'))

    def test_setter_invalid_y_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = "dude"
            Square(2, 4, "dude")

    def test_setter_invalid_y_bool(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = True
            Square(2, 4, True)

    def test_setter_invalid_y_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = None
            Square(2, 4, None)

    def test_setter_invalid_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = (2, 4)
            Square(2, 4, (2, 4))

    def test_setter_invalid_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = [6, 6]
            Square(2, 4, [6, 6])

    def test_setter_invalid_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = {'x': 6}
            Square(2, 4, {'x': 6})

    def test_setter_invalid_y_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = {3, 6, 9}
            Square(2, 4, {3, 6, 9})

    def test_setter_invalid_y_frozenset(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = frozenset({3, 6, 9})
            Square(2, 4, frozenset({3, 6, 9}))

    def test_setter_invalid_y_byte(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = b'dude'
            Square(2, 4, b'dude')

    def test_setter_invalid_y_bytearray(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = bytearray(b'dude')
            Square(2, 4, bytearray(b'dude'))

    def test_setter_invalid_y_memoryview(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.y = memoryview(b'dude')
            Square(2, 4, memoryview(b'dude'))


class TestSquare_area(unittest.TestCase):
    """ tests for Square area method """
    def setUp(self):
        self.instance = Square(2, 4, 8, 12)

    def test_area(self):
        self.assertEqual(Square(4).area(), 16)

    def test_area_INT_MAX_UINT_MAX(self):
        self.instance.width = 2147483647
        self.instance.height = 2147483647
        self.assertEqual(self.instance.area(), 4611686014132420609)

    def test_area_with_argument(self):
        with self.assertRaises(TypeError):
            self.instance.area(24)


class TestSquare_display(unittest.TestCase):
    """ tests for Square display method """
    def test_display_square_2s(self):
        with patch('sys.stdout', new=StringIO()) as comp:
            Square(2).display()
            self.assertEqual(
                comp.getvalue(),
                "##\n##\n"
            )

    def test_display_square_as_square_6s(self):
        with patch('sys.stdout', new=StringIO()) as comp:
            Square(6).display()
            self.assertEqual(
                comp.getvalue(),
                "######\n######\n######\n######\n######\n######\n"
            )

    def test_display_square_2s_2x_4y(self):
        with patch('sys.stdout', new=StringIO()) as comp:
            Square(2, 2, 4).display()
            self.assertEqual(
                comp.getvalue(),
                "\n\n\n\n  ##\n  ##\n"
            )

    def test_display_square_2s_0x_4y(self):
        with patch('sys.stdout', new=StringIO()) as comp:
            Square(2, 0, 4).display()
            self.assertEqual(
                comp.getvalue(),
                "\n\n\n\n##\n##\n"
            )

    def test_display_square_2s_2x_0y(self):
        with patch('sys.stdout', new=StringIO()) as comp:
            Square(2, 2).display()
            self.assertEqual(
                comp.getvalue(),
                "  ##\n  ##\n"
            )

    def test_display_with_argument(self):
        with self.assertRaises(TypeError):
            Square(2).display(2)


class TestSquare_update(unittest.TestCase):
    """ tests for Square update method """
    def setUp(self):
        self.instance = Square(2, 4, 8, 12)

    def test_update_id(self):
        self.instance.update(16)
        self.assertEqual(str(self.instance), "[Square] (16) 4/8 - 2")

    def test_update_size(self):
        self.instance.update(16, 6)
        self.assertEqual(str(self.instance), "[Square] (16) 4/8 - 6")

    def test_update_x(self):
        self.instance.update(16, 6, 10)
        self.assertEqual(str(self.instance), "[Square] (16) 10/8 - 6")

    def test_update_y(self):
        self.instance.update(16, 6, 10, 12)
        self.assertEqual(str(self.instance), "[Square] (16) 10/12 - 6")

    def test_update_no_arguments(self):
        self.instance.update()
        self.assertEqual(str(self.instance), "[Square] (12) 4/8 - 2")

    def test_update_kwargs_id(self):
        self.instance.update(**{'id': 24})
        self.assertEqual(str(self.instance), "[Square] (24) 4/8 - 2")

    def test_update_kwargs_size(self):
        self.instance.update(**{'id': 24, 'size': 4})
        self.assertEqual(str(self.instance), "[Square] (24) 4/8 - 4")

    def test_update_kwargs_x(self):
        self.instance.update(**{'id': 24, 'size': 4, 'x': 8})
        self.assertEqual(str(self.instance), "[Square] (24) 8/8 - 4")

    def test_update_kwargs_y(self):
        self.instance.update(**{'id': 24, 'size': 4, 'x': 8, 'y': 16})
        self.assertEqual(str(self.instance), "[Square] (24) 8/16 - 4")

    def test_update_kwargs_mixed_arguments(self):
        self.instance.update(112, 144, y=66, x=96)
        self.assertEqual(str(self.instance), "[Square] (112) 4/8 - 144")

    def test_update_kwargs_no_matches_found(self):
        self.instance.update(dude=100, surf=200)
        self.assertEqual(str(self.instance), "[Square] (12) 4/8 - 2")

    def test_update_kwargs_mixmatch(self):
        self.instance.update(dude=100, id=144, surf=200, x=60, y=70)
        self.assertEqual(str(self.instance), "[Square] (144) 60/70 - 2")


class TestSquare_updates_invalid_attribute_types(unittest.TestCase):
    """ tests for Square invalid update method attributes """
    def setUp(self):
        self.instance = Square(2, 4, 8, 12)

    def test_update_invalid_size_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, 3.14)

    def test_update_invalid_size_complex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, complex(6))

    def test_update_invalid_size_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, range(6))

    def test_update_invalid_size_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, float('inf'))

    def test_update_invalid_size_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, float('nan'))

    def test_update_invalid_size_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, "dude")

    def test_update_invalid_size_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, True)

    def test_update_invalid_size_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, None)

    def test_update_invalid_size_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, (2, 4))

    def test_update_invalid_size_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, [6, 6])

    def test_update_invalid_size_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, {'width': 6})

    def test_update_invalid_size_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, {3, 6, 9})

    def test_update_invalid_size_frozenset(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, frozenset({3, 6, 9}))

    def test_update_invalid_size_byte(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, b'dude')

    def test_update_invalid_size_bytearray(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, bytearray(b'dude'))

    def test_update_invalid_size_memoryview(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(self.instance.id, memoryview(b'dude'))

    def test_update_invalid_x_float(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                3.14
            )

    def test_update_invalid_x_complex(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                complex(6)
            )

    def test_update_invalid_x_range(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                range(6)
            )

    def test_update_invalid_x_inf(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                float('inf')
            )

    def test_update_invalid_x_nan(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                float('nan')
            )

    def test_update_invalid_x_string(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                "dude"
            )

    def test_update_invalid_x_bool(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                True
            )

    def test_update_invalid_x_none(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                None
            )

    def test_update_invalid_x_tuple(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                (2, 4)
            )

    def test_update_invalid_x_list(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                [6, 6]
            )

    def test_update_invalid_x_dict(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                {'width': 6}
            )

    def test_update_invalid_x_set(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                {3, 6, 9}
            )

    def test_update_invalid_x_frozenset(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                frozenset({3, 6, 9})
            )

    def test_update_invalid_x_byte(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                b'dude'
            )

    def test_update_invalid_x_bytearray(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                bytearray(b'dude')
            )

    def test_update_invalid_x_memoryview(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                memoryview(b'dude')
            )

    def test_update_invalid_y_float(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                self.instance.x,
                3.14
            )

    def test_update_invalid_y_complex(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                self.instance.x,
                complex(6)
            )

    def test_update_invalid_y_range(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                self.instance.x,
                range(6)
            )

    def test_update_invalid_y_inf(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                self.instance.x,
                float('inf')
            )

    def test_update_invalid_y_nan(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                self.instance.x,
                float('nan')
            )

    def test_update_invalid_y_string(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                self.instance.x,
                "dude"
            )

    def test_update_invalid_y_bool(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                self.instance.x,
                True
            )

    def test_update_invalid_y_none(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                self.instance.x,
                None
            )

    def test_update_invalid_y_tuple(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                self.instance.x,
                (2, 4)
            )

    def test_update_invalid_y_list(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                self.instance.x,
                [6, 6]
            )

    def test_update_invalid_y_dict(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                self.instance.x,
                {'width': 6}
            )

    def test_update_invalid_y_set(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                self.instance.x,
                {3, 6, 9}
            )

    def test_update_invalid_y_frozenset(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                self.instance.x,
                frozenset({3, 6, 9})
            )

    def test_update_invalid_y_byte(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                self.instance.x,
                b'dude'
            )

    def test_update_invalid_y_bytearray(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                self.instance.x,
                bytearray(b'dude')
            )

    def test_update_invalid_y_memoryview(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.instance.update(
                self.instance.id,
                self.instance.size,
                self.instance.x,
                memoryview(b'dude')
            )

    def test_update_kwargs_invalid_size_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(size=3.14)

    def test_update_kwargs_invalid_size_complex(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(size=complex(6))

    def test_update_kwargs_invalid_size_range(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(size=range(6))

    def test_update_kwargs_invalid_size_inf(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(size=float('inf'))

    def test_update_kwargs_invalid_size_nan(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(size=float('nan'))

    def test_update_kwargs_invalid_size_string(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(size="dude")

    def test_update_kwargs_invalid_size_bool(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(size=True)

    def test_update_kwargs_invalid_size_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(size=None)

    def test_update_kwargs_invalid_size_tuple(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(size=(2, 4))

    def test_update_kwargs_invalid_size_list(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(size=[6, 6])

    def test_update_kwargs_invalid_size_dict(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(size={'width': 6})

    def test_update_kwargs_invalid_size_set(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(size={3, 6, 9})

    def test_update_kwargs_invalid_size_frozenset(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(size=frozenset({3, 6, 9}))

    def test_update_kwargs_invalid_size_byte(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(size=b'dude')

    def test_update_kwargs_invalid_size_bytearray(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(size=bytearray(b'dude'))

    def test_update_kwargs_invalid_size_memoryview(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.instance.update(size=memoryview(b'dude'))

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


class TestSquare_to_dictionary(unittest.TestCase):
    """ tests for Square to_dictionary method """
    def setUp(self):
        self.instance = Square(2, 4, 8, 12)
        self.inst_dict = {'id': 12, 'size': 2, 'x': 4, 'y': 8}

    def test_to_dictionary(self):
        self.assertDictEqual(self.instance.to_dictionary(), self.inst_dict)

    def test_to_dictionary_update_kwargs(self):
        sq_inst = Square(20, 40, 80, 120)
        sq_inst.update(**self.instance.to_dictionary())
        self.assertNotEqual(hex(id(self.instance)), hex(id(sq_inst)))

    def test_to_dictionary_with_argument(self):
        with self.assertRaises(TypeError):
            self.instance.to_dictionary(12)


if __name__ == "__main__":
    unittest.main()
