from currency_converter import CurrencyConverter

if __name__ == "__main__":
    converter = CurrencyConverter()

    while True:  # Conversion loop
        from_currency = input("Enter currency to convert from (or type 'exit'): ").upper()
        if from_currency == "EXIT":
            break  # Exit the loop

        to_currency = input("Enter currency to convert to: ").upper()
        amount = float(input("Enter amount: "))

        result = converter.convert_currency(from_currency, to_currency, amount)
        if result:
            print(f"{amount} {from_currency} is equal to {result} {to_currency}")
        else:
            print("Conversion failed. Check if currencies are valid.")
