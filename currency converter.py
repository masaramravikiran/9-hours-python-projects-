from request import get 
from pprint import PrettyPrinter

BASE_URL = "https://free.currconv.com/"
API_KEY = "562ddaf40c95f5d8108"

printer = PrettyPrinter()

def get_currencies():
endpoint = f"api/v7/currencies?apikey={API_KEY}"
url = BASE_URL + endpoint
data = get(url).json()['results']

data = list(data.items())

data.sort()
return data

def print_curriences(currencies):
  for currency in curriences:
      name = currency['currencyName']
      _id = currency['id']
      
      symbol = currency.get("currencysymbol","")
      print(f"{_id} - {name} - {symbol}")

def exchange_rate(currency1, currency2):
  endpoint = f"api/v7/convert?q={currency1}_{currency2}&compact=ultra&apiKey={API_KEY}"
  url = BASE_URL + endpoint
  response = get(url)
  
  data  = response.json()
  
  if len(data) == 0:
    print('Invalid currencies.')
    return
  
  return list(data.values())[0]

print(f"{currency1} -> {currency2} {rate}")
return rate
  
def convert(currency1, currency2, amount):
  rate = exchange_rate(currency1, currency2)
  if rate is None:
    return
  
  try:
    amount = float(amount)
  except:
    print("Invalid amount")
    return
  
  coverted_amount = rate * amount
  print(f"{amount} {currency1} is equal to {converted_amount}{currency2}")
  return converted_amount

def main():
  currencies = get_currencies()
  
  print("Welcome to the currency converter!")
  print("list - lists the differnt curreincies")
  print("convert - convert from one currency to another")
  
  print("Rate - get the exchange rate of two currencies")
  
  print()
  
  while True:
    command = input("Enter a command: ").lower()
    if command == "q":
      break
    elif command == "list":
      print_currencies(currencies)
    elif command == "convert":
      currency1 = input("Enter the first currency: ").upper()
      currency2 = input("Enter a currency to convert to:").upper()
      currency2 = input("ENter a currency id: ").upper()
      convert(currency1, currency2, amount)
      
    elif command == "rate":
      currency1 = input("Enter the first currency: ").upper()
      currency2 = input("Enter the first currency: ").upper()
    else:
      print("Unrecognized command!")
      
main()
      