class Category:
    """
    A class to represent a budget category.

    Attributes:
        name (str): The name of the budget category.
        ledger (list): A list to store all transactions.
    """

    def __init__(self, name):
        """
        Initializes the Category with a name and an empty ledger.
        Args:
            name (str): The name of the budget category.
        """
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        """
        Adds a deposit to the ledger.

        Args:
            amount (float): The amount to deposit.
            description (str): The description of the deposit.
        """
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        """
        Adds a withdrawal to the ledger as a negative amount.

        Args:
            amount (float): The amount to withdraw.
            description (str): The description of the withdrawal.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        """
        Calculates the current balance.

        Returns:
            float: The current balance.
        """
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        """
        Transfers an amount to another budget category.

        Args:
            amount (float): The amount to transfer.
            category (Category): The category to transfer the amount to.

        Returns:
            bool: True if the transfer was successful, False otherwise.
        """
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        """
        Checks if funds are available for a withdrawal or transfer.

        Args:
            amount (float): The amount to check.

        Returns:
            bool: True if there are sufficient funds, False otherwise.
        """
        return self.get_balance() >= amount

    def __str__(self):
        """
        Returns a string representation of the category.

        Returns:
            str: The string representation of the category.
        """
        # title = f"{self.name:*^30}\n"
        # items = ""
        # for item in self.ledger:
        #     description = f"{item['description'][:23]:23}"
        #     amount = f"{item['amount']:>7.2f}"
        #     items += f"{description}{amount}\n"
        # total = f"Total: {self.get_balance():.2f}"
        # return title + items + total
        
        title = self.name.center(30, '*') + "\n"
        items = ""
        for item in self.ledger:
            description = item["description"][:23]  
            amount = f"{item['amount']:.2f}"  
            amount = amount.rjust(7) 
            items += f"{description:<23}{amount}\n"
        
        total_balance = "{:.2f}".format(self.get_balance())  
        total = "Total: " + total_balance
    
        return title + items + total

def create_spend_chart(categories):
    """
    Creates a bar chart showing the percentage spent in each category.

    Args:
        categories (list of Category): List of budget categories.

    Returns:
        str: The bar chart as a string.
    """
    # Title
    title = "Percentage spent by category\n"
    
    # Calculate total spent in all categories (only withdrawals)
    total_spent = sum(sum(-item["amount"] for item in category.ledger if item["amount"] < 0) for category in categories)
    
    # Calculate percentages spent in each category
    spent_percentages = [
        int(sum(-item["amount"] for item in category.ledger if item["amount"] < 0) / total_spent * 100) 
        for category in categories
    ]
    
    # Build the chart
    chart = ""
    for i in range(100, -1, -10):
        chart += f"{i:3}|"
        for percent in spent_percentages:
            chart += " o " if percent >= i else "   "
        chart += " \n"
    
    # Add the horizontal line
    chart += "    -" + "---" * len(categories) + "\n"
    
    # Find the longest category name
    max_len = max(len(category.name) for category in categories)
    
    # Add the category names vertically
    names = [category.name.ljust(max_len) for category in categories]
    for x in zip(*names):
        chart += "     " + "  ".join(x) + "  \n"
    
    return title + chart.strip("\n")



food = Category("Food")
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
auto = Category('Auto')
auto.deposit(1000, 'deposit')
auto.withdraw(150, 'car repair')
print(food)
print(clothing)
print(auto)
print(create_spend_chart([food, clothing, auto]))