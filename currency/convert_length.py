class LengthConverter:
    def __init__(self):
        self.base_unit = 'm'  # Our chosen base unit is meters
        self.conversion_factors = {
            'mm': 0.001,  # Millimeters to meters
            'cm': 0.01,  # Centimeters to meters
            'dm': 0.1,  # Decimeters to meters
            'm': 1.0,  # Meters to meters
            'km': 1000,  # Kilometers to meters
            'in': 0.0254,  # Inches to meters
            'ft': 0.3048,  # Feet to meters
            'yd': 0.9144,  # Yards to meters
            'mi': 1609.34,  # Miles to meters
            'nmi': 1852  # Nautical miles to meters
        }

    def convert_length(self, from_unit, to_unit, value):
        if value < 0:  # Check for negative values
            raise ValueError("Length cannot be negative")
        if from_unit not in self.conversion_factors:  # Check for invalid from_unit
            raise KeyError(f"Invalid unit: {from_unit}")
        if to_unit not in self.conversion_factors:  # Check for invalid to_unit
            raise KeyError(f"Invalid unit: {to_unit}")
        if not isinstance(value, (int, float)):  # Check if 'value' is numeric
            raise TypeError("Length value must be numeric")

        if from_unit == self.base_unit:
            value = value / self.conversion_factors[to_unit]  # Convert to base unit from target
        elif to_unit == self.base_unit:
            value = value * self.conversion_factors[from_unit]  # Convert from base unit to target
        else:
            value = value * self.conversion_factors[from_unit] / self.conversion_factors[to_unit]  # Convert other

        return value
