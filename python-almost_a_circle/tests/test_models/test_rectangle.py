#!/usr/bin/python3
# test_rectangle.py
# Travis Adamson
"""Describes the unittests for rectangle.py file

Unittest classes:
    TestRectangle_instantiation - line 25
    TestRectangle_width - line 114
    TestRectangle_height - line 190
    TestRectangle_x - line 266
    TestRectangle_y - line 338
    TestRectangle_order - line 410
    TestRectangle_area - line 438
    TestRectangle_output - line 462
    TestRectangle_update_args - line 551
    TestRectangle_update_kwargs - line 688
    TestRectangle_to_dictionary - line 800
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_instantiation(unittest.TestCase):
    """Unittests that test instantiation of the new class: Rectangle"""

    def test_rectangle_is_also_base(self):
        self.assertIsInstance(Rectangle(15, 20), Base)

    def test_no_argument(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_argument(self):
        with self.assertRaises(TypeError):
            Rectangle(10)

    def test_two_arguments(self):
        rect1 = Rectangle(15, 10)
        rect2 = Rectangle(20, 15)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_three(self):
        rect1 = Rectangle(15, 20, 0)
        rect2 = Rectangle(20, 15, 5)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_four(self):
        rect1 = Rectangle(15, 20, 0, 0)
        rect2 = Rectangle(20, 15, 5, 5)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_with_five(self):
        self.assertEqual(15, Rectangle(15, 20, 0, 0, 15).id)

    def test_too_many_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 6, 1, 2, 3, 10)

    def test_width_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(12, 20, 0, 0, 1).__width)

    def test_height_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(12, 20, 0, 0, 1).__height)

    def test_x_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(12, 20, 0, 0, 1).__x)

    def test_y_private(self):
        with self.assertRaises(AttributeError):
            print(Rectangle(12, 20, 0, 0, 1).__y)

    def test_width_getter(self):
        r = Rectangle(15, 17, 17, 15, 11)
        self.assertEqual(15, r.width)

    def test_height_getter(self):
        r = Rectangle(15, 17, 17, 15, 11)
        self.assertEqual(17, r.height)

    def test_x_getter(self):
        r = Rectangle(15, 17, 17, 15, 11)
        self.assertEqual(17, r.x)

    def test_y_getter(self):
        r = Rectangle(15, 17, 17, 15, 11)
        self.assertEqual(15, r.y)

    def test_width_setter(self):
        r = Rectangle(15, 17, 17, 15, 11)
        r.width = 8
        self.assertEqual(8, r.width)

    def test_height_setter(self):
        r = Rectangle(15, 17, 17, 15, 11)
        r.height = 8
        self.assertEqual(8, r.height)

    def test_x_setter(self):
        r = Rectangle(15, 17, 17, 15, 11)
        r.x = 8
        self.assertEqual(8, r.x)

    def test_y_setter(self):
        r = Rectangle(15, 17, 17, 15, 11)
        r.y = 8
        self.assertEqual(8, r.y)


class TestRectangle_width(unittest.TestCase):
    """Unittests for intialization of Rectangles width"""

    def test_None_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 20)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("bad", 20)

    def test_float_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(5.5, 5)

    def test_complex_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(complex(5), 20)

    def test_dict_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"first": 10, "second": 20}, 20)

    def test_bool_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 2)

    def test_list_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([10, 20, 30], 20)

    def test_set_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({10, 20, 30}, 20)

    def test_tuple_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((10, 20), 20)

    def test_frozenset_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(frozenset({10, 20, 30, 10}), 20)

    def test_range_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(range(3), 20)

    def test_bytes_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(b'Python', 20)

    def test_bytearray_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(bytearray(b'abcd'), 20)

    def test_momoryview_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(memoryview(b'abcd'), 20)

    def test_inf_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('inf'), 20)

    def test_nan_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(float('nan'), 20)

    def test_negative_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 20)

    def test_zero_width(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 20)


class TestRectangle_height(unittest.TestCase):
    """Unittests for intialization of Rectangles height"""

    def test_None_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 20)

    def test_str_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "bad")

    def test_float_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(5, 5.5)

    def test_complex_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, complex(5))

    def test_dict_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(20, {"first": 10, "second": 20})

    def test_bool_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(2, True)

    def test_list_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(20, [10, 20, 30])

    def test_set_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(20, {10, 20, 30})

    def test_tuple_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(20, (10, 20))

    def test_frozenset_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, frozenset({10, 20, 30, 10}))

    def test_range_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, range(3))

    def test_bytes_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, b'Python')

    def test_bytearray_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, bytearray(b'abcd'))

    def test_momoryview_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, memoryview(b'abcd'))

    def test_inf_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, float('inf'))

    def test_nan_height(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, float('nan'))

    def test_negative_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -20)

    def test_zero_height(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(20, 0)


class TestRectangle_x(unittest.TestCase):
    """Unittests for intialization of Rectangles x value"""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, "NONE")

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, "bad")

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, "5.5")

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, {"first": 10, "second": 20})

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, True)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, [10, 20])

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, {10, 20})

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, (10, 20))

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, frozenset({10, 20}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, b'Python')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, bytearray(b'abcd'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, memoryview(b'abcd'))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, float('inf'))

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 20, float('nan'))

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 20, -20)


class TestRectangle_y(unittest.TestCase):
    """Unittests for intialization of Rectangles y value"""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, "NONE")

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, "bad")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, "5.5")

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, {"first": 10, "second": 20})

    def test_bool_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, True)

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, [10, 20])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, {10, 20})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, (10, 20))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, frozenset({10, 20}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, bytearray(b'abcd'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, memoryview(b'abcd'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 20, 0, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 20, 1, -5)


class TestRectangle_order(unittest.TestCase):
    """Unittests for testing Rectangle order of attribute initialization."""

    def test_width_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("inv width", "inv height")

    def test_width_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("inv width", 2, "inv x")

    def test_width_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("inv width", 2, 3, "inv y")

    def test_height_before_x(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "inv height", "inv x")

    def test_height_before_y(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, "inv height", 2, "inv y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 2, "inv x", "inv y")


class TestRectangle_area(unittest.TestCase):
    """Unittests for testing Rectangles area method"""

    def test_area_smaller(self):
        rect1 = Rectangle(20, 3, 0, 0, 0)
        self.assertEqual(60, rect1.area())

    def test_area_larger(self):
        rect1 = Rectangle(1000000000, 3, 0, 0, 0)
        self.assertEqual(3000000000, rect1.area())

    def test_area_changed_values(self):
        rect1 = Rectangle(20, 10, 0, 0, 0)
        rect1.width = 10
        rect1.height = 5
        self.assertEqual(50, rect1.area())

    def test_area_with_arg(self):
        rect1 = Rectangle(10, 10, 0, 0, 0)
        with self.assertRaises(TypeError):
            rect1.area(10)


class TestRectangle_output(unittest.TestCase):
    """Unittests for tessting __str__ and display methods"""

    @staticmethod
    def capture_out(rect, method):
        """Captures and returns text printed to stdout.

        Args:
            rect (Rectangle): The rectangle to print
            method (str): Which method is being used
        Returns:
            The text printed
        """
        cap = io.StringIO()
        sys.stdout = cap
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return cap

    # Test __str__ method first
    def test_str_print_width_height(self):
        rect1 = Rectangle(5, 2)
        correct_result = "[Rectangle] ({}) 0/0 - 5/2".format(rect1.id)
        self.assertEqual(correct_result, rect1.__str__())

    def test_str_width_height(self):
        rect1 = Rectangle(5, 2)
        correct_result = "[Rectangle] ({}) 0/0 - 5/2".format(rect1.id)
        self.assertEqual(correct_result, rect1.__str__())

    def test_str_width_height_x(self):
        rect1 = Rectangle(5, 2, 3)
        correct_result = "[Rectangle] ({}) 3/0 - 5/2".format(rect1.id)
        self.assertEqual(correct_result, rect1.__str__())

    def test_str_width_height_x_y(self):
        rect1 = Rectangle(5, 2, 3, 1)
        correct_result = "[Rectangle] ({}) 3/1 - 5/2".format(rect1.id)
        self.assertEqual(correct_result, rect1.__str__())

    def test_str_width_height_x_y_id(self):
        rect1 = Rectangle(5, 2, 3, 1, 8)
        correct_result = "[Rectangle] (8) 3/1 - 5/2"
        self.assertEqual(correct_result, rect1.__str__())

    def test_str_changed_attrib(self):
        rect1 = Rectangle(5, 2, 3, 1, [8])
        rect1.width = 2
        rect1.height = 8
        rect1.x = 2
        rect1.y = 3
        self.assertEqual("[Rectangle] ([8]) 2/3 - 2/8", str(rect1))

    def test_str_one_arg(self):
        rect1 = Rectangle(5, 2, 3, 1, 8)
        with self.assertRaises(TypeError):
            rect1.__str__(10)

    # Test display method next
    def test_display_width_height(self):
        rect1 = Rectangle(3, 2, 0, 0, 0)
        cap = TestRectangle_output.capture_out(rect1, "display")
        self.assertEqual("###\n###\n", cap.getvalue())

    def test_display_width_height_x(self):
        rect1 = Rectangle(3, 2, 1, 0, 1)
        cap = TestRectangle_output.capture_out(rect1, "display")
        self.assertEqual(" ###\n ###\n", cap.getvalue())

    def test_display_width_height_y(self):
        rect1 = Rectangle(3, 2, 0, 1, 2)
        cap = TestRectangle_output.capture_out(rect1, "display")
        self.assertEqual("\n###\n###\n", cap.getvalue())

    def test_display_width_height_x_y(self):
        rect1 = Rectangle(3, 2, 1, 1, 1)
        cap = TestRectangle_output.capture_out(rect1, "display")
        self.assertEqual("\n ###\n ###\n", cap.getvalue())

    def test_display_one_arg(self):
        rect1 = Rectangle(3, 2, 1, 1, 1)
        with self.assertRaises(TypeError):
            rect1.display(10)


class TestRectangle_update_args(unittest.TestCase):
    """Unittests for testing update using args"""

    def test_update_args_empty(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        rect1.update()
        self.assertEqual("[Rectangle] (20) 20/20 - 20/20", str(rect1))

    def test_update_args_one(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        rect1.update(10)
        self.assertEqual("[Rectangle] (10) 20/20 - 20/20", str(rect1))

    def test_update_args_two(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        rect1.update(10, 2)
        self.assertEqual("[Rectangle] (10) 20/20 - 2/20", str(rect1))

    def test_update_args_three(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        rect1.update(10, 2, 3)
        self.assertEqual("[Rectangle] (10) 20/20 - 2/3", str(rect1))

    def test_update_args_four(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        rect1.update(10, 2, 3, 4)
        self.assertEqual("[Rectangle] (10) 4/20 - 2/3", str(rect1))

    def test_update_args_five(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        rect1.update(10, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (10) 4/5 - 2/3", str(rect1))

    def test_update_args_more_than_five(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        rect1.update(10, 2, 3, 4, 5, 6)
        self.assertEqual("[Rectangle] (10) 4/5 - 2/3", str(rect1))

    def test_update_args_None_id(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        rect1.update(None)
        correct = "[Rectangle] ({}) 20/20 - 20/20".format(rect1.id)
        self.assertEqual(correct, str(rect1))

    def test_update_args_None_id_and_more(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        rect1.update(None, 3, 4, 3)
        correct = "[Rectangle] ({}) 3/20 - 3/4".format(rect1.id)
        self.assertEqual(correct, str(rect1))

    def test_update_args_twice(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        rect1.update(10, 2, 3, 4, 5, 6)
        rect1.update(6, 5, 4, 3, 2, 10)
        self.assertEqual("[Rectangle] (6) 3/2 - 5/4", str(rect1))

    def test_update_args_invalid_width_type(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect1.update(10, "bad")

    def test_update_args_width_zero(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect1.update(10, 0)

    def test_update_args_width_negative(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect1.update(10, -5)

    def test_update_args_invalid_height_type(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect1.update(10, 2, "bad")

    def test_update_args_height_zero(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect1.update(10, 1, 0)

    def test_update_args_height_negative(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect1.update(10, 1, -5)

    def test_update_args_invalid_x_type(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect1.update(10, 2, 3, "bad")

    def test_update_args_x_negative(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect1.update(10, 1, 2, -6)

    def test_update_args_invalid_y(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect1.update(10, 2, 3, 4, "bad")

    def test_update_args_y_negative(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect1.update(10, 1, 2, 3, -6)

    def test_update_args_width_before_height(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect1.update(10, "bad", "bad")

    def test_update_args_width_before_x(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect1.update(10, "bad", 1, "bad")

    def test_update_args_width_before_y(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect1.update(10, "bad", 1, 2, "bad")

    def test_update_args_height_before_x(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect1.update(10, 1, "bad", "bad")

    def test_update_args_height_before_y(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect1.update(10, 1, "bad", 1, "bad")

    def test_update_args_x_before_y(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect1.update(10, 1, 2, "bad", "bad")


class TestRectangle_update_kwargs(unittest.TestCase):
    """Unittests for testing update by kwargs on the Rectangle class."""

    def test_update_kwargs_one(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        rect1.update(id=1)
        self.assertEqual("[Rectangle] (1) 20/20 - 20/20", str(rect1))

    def test_update_kwargs_two(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        rect1.update(width=2, id=1)
        self.assertEqual("[Rectangle] (1) 20/20 - 2/20", str(rect1))

    def test_update_kwargs_three(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        rect1.update(width=2, height=3, id=10)
        self.assertEqual("[Rectangle] (10) 20/20 - 2/3", str(rect1))

    def test_update_kwargs_four(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        rect1.update(id=10, x=1, height=2, y=3, width=4)
        self.assertEqual("[Rectangle] (10) 1/3 - 4/2", str(rect1))

    def test_update_kwargs_five(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        rect1.update(y=5, x=8, id=10, width=1, height=2)
        self.assertEqual("[Rectangle] (10) 8/5 - 1/2", str(rect1))

    def test_update_kwargs_None_id(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        rect1.update(id=None)
        correct = "[Rectangle] ({}) 20/20 - 20/20".format(rect1.id)
        self.assertEqual(correct, str(rect1))

    def test_update_kwargs_None_id_and_more(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        rect1.update(id=None, height=7, y=9)
        correct = "[Rectangle] ({}) 20/9 - 20/7".format(rect1.id)
        self.assertEqual(correct, str(rect1))

    def test_update_kwargs_twice(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        rect1.update(id=10, x=1, height=2)
        rect1.update(y=3, height=15, width=2)
        self.assertEqual("[Rectangle] (10) 1/3 - 2/15", str(rect1))

    def test_update_kwargs_invalid_width_type(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            rect1.update(width="bad")

    def test_update_kwargs_width_zero(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect1.update(width=0)

    def test_update_kwargs_width_negative(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            rect1.update(width=-5)

    def test_update_kwargs_invalid_height_type(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            rect1.update(height="bad")

    def test_update_kwargs_height_zero(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect1.update(height=0)

    def test_update_kwargs_height_negative(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            rect1.update(height=-5)

    def test_update_kwargs_inavlid_x_type(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            rect1.update(x="bad")

    def test_update_kwargs_x_negative(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            rect1.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            rect1.update(y="bad")

    def test_update_kwargs_y_negative(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            rect1.update(y=-5)

    def test_update_args_and_kwargs(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        rect1.update(10, 2, height=4, y=6)
        self.assertEqual("[Rectangle] (10) 20/20 - 2/20", str(rect1))

    def test_update_kwargs_wrong_keys(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        rect1.update(a=5, b=10)
        self.assertEqual("[Rectangle] (20) 20/20 - 20/20", str(rect1))

    def test_update_kwargs_some_wrong_keys(self):
        rect1 = Rectangle(20, 20, 20, 20, 20)
        rect1.update(height=5, id=10, a=1, b=54, x=19, y=7)
        self.assertEqual("[Rectangle] (10) 19/7 - 20/5", str(rect1))


class TestRectangle_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method"""

    def test_to_dictionary_out(self):
        rect1 = Rectangle(10, 2, 1, 9, 5)
        correct = {'x': 1, 'y': 9, 'id': 5, 'height': 2, 'width': 10}
        self.assertDictEqual(correct, rect1.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        rect1 = Rectangle(10, 2, 1, 9, 5)
        rect2 = Rectangle(5, 9, 1, 2, 10)
        rect2.update(**rect1.to_dictionary())
        self.assertNotEqual(rect1, rect2)

    def test_to_dictionary_arg(self):
        rect1 = Rectangle(10, 2, 4, 1, 2)
        with self.assertRaises(TypeError):
            rect1.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
