def print_balance(): 
    balance = 1000
    print("Your balance is " + str(balance))
    return balance

def deduct(amount):
    print("Your new balance is " + str(print_balance() - amount))

def calculate_interest_on_savings():
  savings = 500
  print("You will gain interest on: " + str(savings))
  def calculate_taxes():
    tax_amount = savings * 0.13
    print("You will be taxed: " + str(tax_amount))
  calculate_taxes()

print_balance()
deduct(500)
calculate_interest_on_savings()