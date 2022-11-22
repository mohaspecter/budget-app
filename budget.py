class Category:
    def __init__(self, description):
        self.description = description
        self.ledger = []
        self.balance = 0.0
    def __repr__(self):
        header = self.description.center(30, "*") + "\n"
        ledger = ""
        for item in self.ledger:
            # format description and amount
            line_description = "{:<23}".format(item["description"])
            line_amount = "{:>7.2f}".format(item["amount"])
            # Truncate ledger description and amount to 23 and 7 characters respectively
            ledger += "{}{}\n".format(line_description[:23], line_amount[:7])
        total = "Total: {:.2f}".format(self.balance)
        return header + ledger + total

#A deposit method that accepts an amount and description. If no description is given, it should default to an empty string. 
#The method should append an object to the ledger list in the form of {"amount": amount, "description": description}.
    def deposit(self,amount,description=""):
      self.balance = self.balance + amount
      self.ledger.append({"amount": amount, "description": description})

#A check_funds method that accepts an amount as an argument. 
#It returns False if the amount is greater than the balance of the budget category and returns True otherwise. 
#This method should be used by both the withdraw method and transfer method.


#A withdraw method that is similar to the deposit method, but the amount passed in should be stored in the ledger as a negative number. 
#If there are not enough funds, nothing should be added to the ledger. This method should return True if the withdrawal took place, and False otherwise.
    def withdraw(self,amount,description=""):
      def check_funds(self,amount):
        if amount>self.balance:
          return False
        else:
          return True
      
      chk = check_funds(self,amount)
      if chk==False:
        return False
      else:
        self.balance = self.balance - amount
        self.ledger.append({"amount": -1 * amount, "description": description})
        return True

#A get_balance method that returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
    def get_balance(self):
      return self.balance

#The method should add a withdrawal with the amount and the description "Transfer to [Destination Budget Category]". 
#The method should then add a deposit to the other budget category with the amount and the description "Transfer from [Source Budget Category]". 
#If there are not enough funds, nothing should be added to either ledgers. This method should return True if the transfer took place, and False otherwise.
    def transfer(self,amount,category_name):
      source_cat = "Transfer to "+category_name.description
      target_cat = "Transfer from"+self.description
      try: 
        withdrawal = self.withdraw(amount,source_cat)
        category_name.deposit(category_name, amount, target_cat)
        return True
      except:
        return False

def create_spend_chart(categories):
    spent_amounts = []
    # Get total spent in each category
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        spent_amounts.append(round(spent, 2))

    # Calculate percentage rounded down to the nearest 10
    total = round(sum(spent_amounts), 2)
    spent_percentage = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spent_amounts))

    # Create the bar chart substrings
    header = "Percentage spent by category\n"

    chart = ""
    for value in reversed(range(0, 101, 10)):
        chart += str(value).rjust(3) + '|'
        for percent in spent_percentage:
            if percent >= value:
                chart += " o "
            else:
                chart += "   "
        chart += " \n"

    footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
    descriptions = list(map(lambda category: category.description, categories))
    max_length = max(map(lambda description: len(description), descriptions))
    descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
    for x in zip(*descriptions):
        footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

    return (header + chart + footer).rstrip("\n")
