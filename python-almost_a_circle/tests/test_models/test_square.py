#!/usr/bin/python3
# test_square.py
# Travis Adamson
"""Describes the unittests for square.py file

Unittest classes:
    TestSquare_instantiation - line 26
    TestSquare_size - line 98
    TestSquare_x - line 174
    TestSquare_y - line 246
    TestSquare_order - line 318
    TestSquare_area - line 334
    TestSquare_output - line 355
    TestSquare_update_args - line 438
    TestSquare_update_kwargs - line 550
    TestSquare_to_dictionary - line 652
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittests that test instantiation of the new class: Square"""

    def test_square_is_also_base(self):
        self.assertIsInstance(Square(15), Base)

    def test_square_is_also_rectangle(self):
        self.assertIsInstance(Square(15), Rectangle)

    def test_no_argument(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_argument(self):
        sq1 = Square(10)
        sq2 = Square(15)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_two_arguments(self):
        sq1 = Square(15, 1)
        sq2 = Square(20, 1)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_three(self):
        sq1 = Square(15, 1, 0)
        sq2 = Square(20, 1, 5)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_four(self):
        self.assertEqual(15, Square(20, 15, 5, 15).id)

    def test_too_many_arguments(self):
        with self.assertRaises(TypeError):
            Square(5, 6, 1, 2, 3, 10)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(12, 20, 0, 1).__size)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Square(12, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Square(12, 20, 0, 1).__y)

    def test_size_getter(self):
        self.assertEqual(15, Square(15, 17, 17, 11).size)

    def test_width_getter(self):
        sq1 = Square(10, 5, 3, 1)
        sq1.size = 4
        self.assertEqual(4, sq1.width)

    def test_height_getter(self):
        sq1 = Square(10, 5, 3, 1)
        sq1.size = 4
        self.assertEqual(4, sq1.height)

    def test_x_getter(self):
        self.assertEqual(0, Square(5).x)

    def test_y_getter(self):
        self.assertEqual(0, Square(5).y)

    def test_size_setter(self):
        sq1 = Square(15, 17, 15, 11)
        sq1.size = 4
        self.assertEqual(4, sq1.size)


class TestSquare_size(unittest.TestCase):
    """Unittests for intialization of Squares size"""

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("bad")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_complex_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5))

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"first": 10, "second": 20})

    def test_bool_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([10, 20, 30])

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({10, 20, 30})

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((10, 20))

    def test_frozenset_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({10, 20, 30, 10}))

    def test_range_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(3))

    def test_bytes_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Python')

    def test_bytearray_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'abcd'))

    def test_momoryview_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'abcd'))

    def test_inf_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_nan_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-10)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)


class TestSquare_x(unittest.TestCase):
    """Unittests for intialization of Square x value"""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, "bad")

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, 5.5)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, {"first": 10, "second": 20})

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, True)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, [10, 20])

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, {10, 20})

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, (10, 20))

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, frozenset({10, 20}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, b'Python')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, bytearray(b'abcd'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, memoryview(b'abcd'))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, float('inf'))

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(10, float('nan'))

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(10, -20)


class TestSquare_y(unittest.TestCase):
    """Unittests for intialization of Square y value"""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, "bad")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, {"first": 10, "second": 20})

    def test_bool_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, True)

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, [10, 20])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, {10, 20})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, (10, 20))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, frozenset({10, 20}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, bytearray(b'abcd'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, memoryview(b'abcd'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(10, 0, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(10, 1, -5)


class TestSquare_order(unittest.TestCase):
    """Unittests for testing Square order of attribute initialization."""

    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("inv size", "inv x")

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("inv size", 3, "inv y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "inv x", "inv y")


class TestSquare_area(unittest.TestCase):
    """Unittests for testing Square area"""

    def test_area_smaller(self):
        self.assertEqual(400, Square(20, 0, 0, 1).area())

    def test_area_larger(self):
        sq1 = Square(1000000000, 0, 0, 1)
        self.assertEqual(1000000000000000000, sq1.area())

    def test_area_changed_size(self):
        sq1 = Square(10, 0, 0, 1)
        sq1.size = 5
        self.assertEqual(25, sq1.area())

    def test_area_with_arg(self):
        sq1 = Square(10, 0, 0, 1)
        with self.assertRaises(TypeError):
            sq1.area(15)


class TestSquare_output(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Square class."""

    @staticmethod
    def cap_out(sq, method):
        """Captures and returns text printed to stdout.

        Args:
            sq (Square): The Square ot print to stdout.
            method (str): The method to run on sq.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        cap = io.StringIO()
        sys.stdout = cap
        if method == "print":
            print(sq)
        else:
            sq.display()
        sys.stdout = sys.__stdout__
        return cap

    def test_str_print_size(self):
        sq1 = Square(4)
        cap = TestSquare_output.cap_out(sq1, "print")
        correct = "[Square] ({}) 0/0 - 4\n".format(sq1.id)
        self.assertEqual(correct, cap.getvalue())

    def test_str_size_x(self):
        sq1 = Square(5, 5)
        correct = "[Square] ({}) 5/0 - 5".format(sq1.id)
        self.assertEqual(correct, sq1.__str__())

    def test_str_size_x_y(self):
        sq1 = Square(7, 4, 22)
        correct = "[Square] ({}) 4/22 - 7".format(sq1.id)
        self.assertEqual(correct, str(sq1))

    def test_str_size_x_y_id(self):
        sq1 = Square(2, 88, 4, 19)
        self.assertEqual("[Square] (19) 88/4 - 2", str(sq1))

    def test_str_changed_attributes(self):
        sq1 = Square(7, 0, 0, [4])
        sq1.size = 15
        sq1.x = 8
        sq1.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(sq1))

    def test_str_one_arg(self):
        sq1 = Square(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            sq1.__str__(1)

    # Test display method
    def test_display_size(self):
        sq1 = Square(2, 0, 0, 9)
        cap = TestSquare_output.cap_out(sq1, "display")
        self.assertEqual("##\n##\n", cap.getvalue())

    def test_display_size_x(self):
        sq1 = Square(3, 1, 0, 18)
        cap = TestSquare_output.cap_out(sq1, "display")
        self.assertEqual(" ###\n ###\n ###\n", cap.getvalue())

    def test_display_size_y(self):
        sq1 = Square(4, 0, 1, 9)
        cap = TestSquare_output.cap_out(sq1, "display")
        display = "\n####\n####\n####\n####\n"
        self.assertEqual(display, cap.getvalue())

    def test_display_size_x_y(self):
        sq1 = Square(2, 3, 2, 1)
        cap = TestSquare_output.cap_out(sq1, "display")
        display = "\n\n   ##\n   ##\n"
        self.assertEqual(display, cap.getvalue())

    def test_display_one_arg(self):
        sq1 = Square(3, 4, 5, 2)
        with self.assertRaises(TypeError):
            sq1.display(1)


class TestSquare_update_args(unittest.TestCase):
    """Unittests for testing update args method of the Square class."""

    def test_update_args_zero(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(sq1))

    def test_update_args_one(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update(10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(sq1))

    def test_update_args_two(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update(10, 2)
        self.assertEqual("[Square] (10) 10/10 - 2", str(sq1))

    def test_update_args_three(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update(10, 2, 3)
        self.assertEqual("[Square] (10) 3/10 - 2", str(sq1))

    def test_update_args_four(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update(10, 2, 3, 4)
        self.assertEqual("[Square] (10) 3/4 - 2", str(sq1))

    def test_update_args_more_than_four(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update(10, 2, 3, 4, 5)
        self.assertEqual("[Square] (10) 3/4 - 2", str(sq1))

    def test_update_args_width_setter(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update(10, 2)
        self.assertEqual(2, sq1.width)

    def test_update_args_height_setter(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update(10, 2)
        self.assertEqual(2, sq1.height)

    def test_update_args_None_id(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update(None)
        correct = "[Square] ({}) 10/10 - 10".format(sq1.id)
        self.assertEqual(correct, str(sq1))

    def test_update_args_None_id_and_more(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update(None, 4, 5)
        correct = "[Square] ({}) 5/10 - 4".format(sq1.id)
        self.assertEqual(correct, str(sq1))

    def test_update_args_twice(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update(10, 2, 3, 4)
        sq1.update(4, 3, 2, 10)
        self.assertEqual("[Square] (4) 2/10 - 3", str(sq1))

    def test_update_args_invalid_size_type(self):
        sq1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq1.update(10, "invalid")

    def test_update_args_size_zero(self):
        sq1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq1.update(10, 0)

    def test_update_args_size_negative(self):
        sq1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq1.update(10, -4)

    def test_update_args_invalid_x(self):
        sq1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq1.update(10, 1, "invalid")

    def test_update_args_x_negative(self):
        sq1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sq1.update(98, 1, -4)

    def test_update_args_invalid_y(self):
        sq1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq1.update(10, 1, 2, "invalid")

    def test_update_args_y_negative(self):
        sq1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sq1.update(98, 1, 2, -4)

    def test_update_args_size_before_x(self):
        sq1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq1.update(10, "bad", "bad")

    def test_update_args_size_before_y(self):
        sq1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq1.update(10, "bad", 2, "bad")

    def test_update_args_x_before_y(self):
        sq1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq1.update(10, 1, "bad", "bad")


class TestSquare_update_kwargs(unittest.TestCase):
    """Unittests for testing update with kwargs"""

    def test_update_kwargs_one(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(sq1))

    def test_update_kwargs_two(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update(size=1, id=2)
        self.assertEqual("[Square] (2) 10/10 - 1", str(sq1))

    def test_update_kwargs_three(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update(y=1, size=3, id=10)
        self.assertEqual("[Square] (10) 10/1 - 3", str(sq1))

    def test_update_kwargs_four(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update(id=10, x=1, y=3, size=4)
        self.assertEqual("[Square] (10) 1/3 - 4", str(sq1))

    def test_update_kwargs_width_setter(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update(id=10, size=8)
        self.assertEqual(8, sq1.width)

    def test_update_kwargs_height_setter(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update(id=10, size=9)
        self.assertEqual(9, sq1.height)

    def test_update_kwargs_None_id(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(sq1.id)
        self.assertEqual(correct, str(sq1))

    def test_update_kwargs_None_id_and_more(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update(id=None, size=7, x=18)
        correct = "[Square] ({}) 18/10 - 7".format(sq1.id)
        self.assertEqual(correct, str(sq1))

    def test_update_kwargs_twice(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update(id=10, x=1)
        sq1.update(y=3, x=15, size=2)
        self.assertEqual("[Square] (10) 15/3 - 2", str(sq1))

    def test_update_kwargs_invalid_size(self):
        sq1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            sq1.update(size="bad")

    def test_update_kwargs_size_zero(self):
        sq1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq1.update(size=0)

    def test_update_kwargs_size_negative(self):
        sq1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            sq1.update(size=-3)

    def test_update_kwargs_invalid_x(self):
        sq1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            sq1.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        sq1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            sq1.update(x=-5)

    def test_update_kwargs_invalid_y(self):
        sq1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            sq1.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        sq1 = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            sq1.update(y=-5)

    def test_update_args_and_kwargs(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update(10, 2, y=6)
        self.assertEqual("[Square] (10) 10/10 - 2", str(sq1))

    def test_update_kwargs_wrong_keys(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(sq1))

    def test_update_kwargs_some_wrong_keys(self):
        sq1 = Square(10, 10, 10, 10)
        sq1.update(size=5, id=10, a=1, b=54)
        self.assertEqual("[Square] (10) 10/10 - 5", str(sq1))


class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Square class."""

    def test_to_dictionary_output(self):
        sq1 = Square(10, 2, 1, 1)
        correct = {'id': 1, 'x': 2, 'size': 10, 'y': 1}
        self.assertDictEqual(correct, sq1.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        sq1 = Square(10, 2, 1, 2)
        sq2 = Square(1, 2, 10)
        sq2.update(**sq1.to_dictionary())
        self.assertNotEqual(sq1, sq2)

    def test_to_dictionary_arg(self):
        sq1 = Square(10, 10, 10, 10)
        with self.assertRaises(TypeError):
            sq1.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
