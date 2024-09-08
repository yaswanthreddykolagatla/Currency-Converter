# Simple Currency Converter for multiple currencies
def convert_currency(amount, from_currency, to_currency, exchange_rates):
   
    if from_currency in exchange_rates and to_currency in exchange_rates:
        # Convert the amount from 'from_currency' to USD, then to 'to_currency'
        amount_in_usd = amount / exchange_rates[from_currency]
        return amount_in_usd * exchange_rates[to_currency]
    else:
        return None  # Unsupported currency conversion

# Dictionary of exchange rates relative to USD
exchange_rates = {
    'USD': 1.00,   # Base currency is USD
    'INR': 82.50,  # 1 USD = 82.50 INR
    'PKR': 305.00, # 1 USD = 305.00 PKR
    'EUR': 0.92,   # 1 USD = 0.92 EUR
    'CNY': 7.30,   # 1 USD = 7.30 CNY
    'JPY': 146.00, # 1 USD = 146.00 JPY
    'GBP': 0.79,   # 1 USD = 0.79 GBP
    'AUD': 1.55,   # 1 USD = 1.55 AUD
    'CAD': 1.35,   # 1 USD = 1.35 CAD
    'CHF': 0.89,   # 1 USD = 0.89 CHF
    'KRW': 1315.00 # 1 USD = 1315.00 KRW
}

# Example usage with user input:
try:
    amount = float(input("Enter the amount you want to convert: "))  # Amount to convert
    from_currency = input("Enter the currency you have (USD, INR, PKR, EUR, CNY, JPY, GBP, AUD, CAD, CHF, KRW): ").upper()
    to_currency = input("Enter the currency you want to convert to (USD, INR, PKR, EUR, CNY, JPY, GBP, AUD, CAD, CHF, KRW): ").upper()

    # Call the conversion function
    converted_amount = convert_currency(amount, from_currency, to_currency, exchange_rates)

    if converted_amount is not None:
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
    else:
        print("Currency conversion not supported for the selected currencies.")
except ValueError:
    print("Invalid input. Please enter a valid number for the amount.")
