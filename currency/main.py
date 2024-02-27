import argparse
import sys

from convert_currency import CurrencyConverter
from convert_length import LengthConverter


def main():
    if len(sys.argv) > 1:
        parser = argparse.ArgumentParser(description="Choose conversion type and parameters.")
        parser.add_argument("conversion_type", choices=['1', '2'], help="1 for currency, 2 for length")
        parser.add_argument("--from", dest='from_unit',  help="Unit/currency to convert from")
        parser.add_argument("--to", dest='to_unit',  help="Unit/currency to convert to")
        parser.add_argument("--amount", type=float,  help="Amount to convert")

        args = parser.parse_args()

        # Process command-line arguments if provided
        if args.conversion_type:
            if args.conversion_type == '1':
                currency_converter = CurrencyConverter()
                result = currency_converter.convert_currency(args.from_unit, args.to_unit, args.amount)
                if result:
                    print(f"{args.amount} {args.from_unit} is equal to {result} {args.to_unit}")
                else:
                    print("Conversion failed. Check if currencies are valid.")

            elif args.conversion_type == '2':
                length_converter = LengthConverter()
                result = length_converter.convert_length(args.from_unit, args.to_unit, args.amount)
                if result:
                    rounded_result = round_to_nearest_nonzero(result)
                    rounded_value = round_to_nearest_nonzero(args.amount)
                    print(f"{rounded_value} {args.from_unit} is equal to {rounded_result} {args.to_unit}")
                else:
                    print("Conversion failed. Check if units are valid.")

    else:  # Fallback to interactive mode if no command-line arguments
        while True:
            choice = input("Choose conversion type (1: Currency, 2: Length, 3: Exit): ")

            if choice == '1':
                currency_converter = CurrencyConverter()
                currency_conversion_loop(currency_converter)

            elif choice == '2':
                length_converter = LengthConverter()
                length_conversion_loop(length_converter)

            elif choice == '3':
                print("Exiting program...")
                break

            else:
                print("Invalid choice. Please try again.")


def currency_conversion_loop(currency_converter):
    while True:  # Conversion loop
        from_currency = input("Enter currency to convert from (or type 'exit'): ").upper()
        if from_currency == "EXIT":
            break  # Exit the loop

        to_currency = input("Enter currency to convert to: ").upper()
        amount = float(input("Enter amount: "))

        result = currency_converter.convert_currency(from_currency, to_currency, amount)
        if result:
            print(f"{amount} {from_currency} is equal to {result} {to_currency}")
        else:
            print("Conversion failed. Check if currencies are valid.")


def length_conversion_loop(length_converter):
    while True:
        from_unit = input("Enter unit to convert from (or type 'exit'): ").lower()
        if from_unit == "exit":
            break

        to_unit = input("Enter unit to convert to: ").lower()
        value = float(input("Enter amount: "))

        result = length_converter.convert_length(from_unit, to_unit, value)
        if result:
            rounded_result = round_to_nearest_nonzero(result)
            rounded_value = round_to_nearest_nonzero(value)  # Apply formatting to 'value'
            print(f"{rounded_value} {from_unit} is equal to {rounded_result} {to_unit}")
        else:
            print("Conversion failed. Check if units are valid.")


def round_to_nearest_nonzero(number, max_decimal_places=12):
    """Rounds a number to a maximum number of decimal places and returns a string representation."""

    if number == 0:
        return "0"

    str_number = f"{number:.{max_decimal_places}f}"  # Format as a string
    return str_number.rstrip("0").rstrip(".")  # Strip trailing zeros and decimal (if needed)


if __name__ == "__main__":
    main()
