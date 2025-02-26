import csv

def load_currency_rates(filename):
    currency_rates = {}
    try:
        with open(filename, mode='r', encoding='ISO-8859-1') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header
            for row in reader:
                currency, _, rate = row  # Adjusted to read the third column
                currency_rates[currency] = float(rate)
    except FileNotFoundError:
        print("Error: The file currency.csv was not found.")
        exit()
    return currency_rates

def read_conversion_rate(filename, currency):
    rates = load_currency_rates(filename)
    return rates.get(currency, None)

def convert_currency(amount, currency, rates):
    if currency in rates:
        return amount * rates[currency]
    else:
        print("Error: Currency not found in exchange rates.")
        exit()

if __name__ == "__main__":
    filename = "currency.csv"
    rates = load_currency_rates(filename)
    
    try:
        dollars = float(input("How much dollar do you have? "))
        currency = input("What currency you want to have? ").upper()
        conversion_rate = read_conversion_rate(filename, currency)
        
        if conversion_rate:
            converted_amount = convert_currency(dollars, currency, rates)
            print(f"\nDollar: {int(dollars)} USD")
            print(f"{currency}: {converted_amount}")
        else:
            print("Error: Currency not found in the file.")
    except ValueError:
        print("Error: Please enter a valid number for the dollar amount.")
