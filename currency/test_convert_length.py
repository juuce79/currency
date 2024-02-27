import unittest
import inspect

from convert_length import LengthConverter


class LengthConversionTests(unittest.TestCase):

    def setUp(self):  # Instantiate a converter before each test
        self.converter = LengthConverter()

    @staticmethod
    def print_output(from_unit, to_unit, value, expected, actual):
        test_method_name = inspect.stack()[1][3]  # Get the calling test method's name
        print(f"{test_method_name}: {value} {from_unit} = {actual} {to_unit} (Expected: {expected})")

    def test_centimeters_to_meters(self):
        result = self.converter.convert_length('cm', 'm', 100)
        self.assertAlmostEqual(result, 1, places=4)
        self.print_output('cm', 'm', 100, 1.0, result)  # Pass 'result' here

        result = self.converter.convert_length('cm', 'm', 500.5)
        self.assertAlmostEqual(result, 5.005, places=4)
        self.print_output('cm', 'm', 500.5, 5.005, result)  # Pass 'result' here

    def test_meters_to_kilometers(self):
        result = self.converter.convert_length('m', 'km', 1000)
        self.assertAlmostEqual(result, 1, places=4)
        self.print_output('m', 'km', 1000, 1, result)

        result = self.converter.convert_length('m', 'km', 7500)
        self.assertAlmostEqual(result, 7.5, places=4)
        self.print_output('m', 'km', 7500, 7.5, result)

    def test_inches_to_feet(self):
        result = self.converter.convert_length('in', 'ft', 12)
        self.assertAlmostEqual(result, 1, places=4)
        self.print_output('in', 'ft', 12, 1, result)

        result = self.converter.convert_length('in', 'ft', 36)
        self.assertAlmostEqual(result, 3, places=4)
        self.print_output('in', 'ft', 36, 3, result)

    def test_centimeters_to_inches(self):
        result = self.converter.convert_length('cm', 'in', 2.54)
        self.assertAlmostEqual(result, 1, places=4)
        self.print_output('cm', 'in', 2.54, 1, result)

        result = self.converter.convert_length('cm', 'in', 150)
        self.assertAlmostEqual(result, 59.0551, places=4)
        self.print_output('cm', 'in', 150, 59.0551, result)

    def test_feet_to_meters(self):
        result = self.converter.convert_length('ft', 'm', 3.281)
        self.assertAlmostEqual(result, 1, places=4)
        self.print_output('ft', 'm', 3.281, 1, result)

        result = self.converter.convert_length('ft', 'm', 10)
        self.assertAlmostEqual(result, 3.048, places=4)
        self.print_output('ft', 'm', 10, 3.048, result)

    def test_millimeters_to_meters(self):
        result = self.converter.convert_length('mm', 'm', 1000)
        self.assertAlmostEqual(result, 1, places=4)
        self.print_output('mm', 'm', 1000, 1, result)

    def test_meters_to_millimeters(self):
        result = self.converter.convert_length('m', 'mm', 0.5)
        self.assertAlmostEqual(result, 500, places=4)
        self.print_output('m', 'mm', 0.5, 500, result)

    def test_yards_to_feet(self):
        result = self.converter.convert_length('yd', 'ft', 2)
        self.assertAlmostEqual(result, 6, places=4)
        self.print_output('yd', 'ft', 2, 6, result)

    def test_miles_to_meters(self):
        result = self.converter.convert_length('mi', 'm', 0.5)
        self.assertAlmostEqual(result, 804.672, places=2)
        self.print_output('mi', 'm', 0.5, 804.672, result)

    def test_nautical_miles_to_kilometers(self):
        result = self.converter.convert_length('nmi', 'km', 3)
        self.assertAlmostEqual(result, 5.556, places=3)
        self.print_output('nmi', 'km', 3, 5.556, result)

    def test_same_unit_conversion(self):
        """Tests that conversion between the same units returns the original value"""
        result = self.converter.convert_length('cm', 'cm', 100)
        self.assertEqual(result, 100)  # Expect the original value unchanged
        self.print_output('cm', 'cm', 100, 100, result)

    def test_zero_conversion(self):
        result = self.converter.convert_length('cm', 'm', 0)
        self.assertAlmostEqual(result, 0)
        self.print_output('cm', 'm', 0, 0, result)

    def test_negative_input(self):
        with self.assertRaises(ValueError):  # Expect a ValueError
            self.converter.convert_length('ft', 'm', -10)
            print(f"{ValueError} is not a number")

    def test_invalid_units(self):
        with self.assertRaises(KeyError):
            self.converter.convert_length('xyz', 'km', 5)
            print(f"{KeyError} is not a valid unit")

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            self.converter.convert_length('cm', 'm', 'hello')
            print(f"{TypeError} is not a valid value")


if __name__ == '__main__':
    unittest.main()
