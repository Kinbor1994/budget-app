# Budget App

## Description

This project is a budget management application that allows you to create and manage different budget categories such as food, clothing, and entertainment. Each category has a ledger to keep track of deposits and withdrawals.

## Features

- **Deposit**: Adds money to a budget category with an optional description.
- **Withdraw**: Withdraws money from a budget category. If there are insufficient funds, the transaction is canceled.
- **Get Balance**: Returns the current balance of a budget category.
- **Transfer**: Transfers money from one budget category to another.
- **Check Funds**: Checks if a budget category has sufficient funds for a given transaction.

## Usage

Here is an example of how to use the application:

```python
from budget import Category, create_spend_chart

# Create categories
food = Category("Food")
clothing = Category("Clothing")
entertainment = Category("Entertainment")

# Make deposits and withdrawals
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")

# Transfer funds between categories
food.transfer(50, clothing)

# Print category details
print(food)
print(clothing)

# Create spending chart
chart = create_spend_chart([food, clothing, entertainment])
print(chart)
```

### Output

```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96

***********Clothing***********
Transfer from Food       50.00
Total: 50.00

Percentage spent by category
100|  
 90|  
 80|  
 70|  
 60|  
 50|  
 40|  
 30|  
 20|    o   
 10| o  o   
  0| o  o  o  
    ----------
     F  C  E  
     o  l  n  
     o  o  t  
     d  t  e  
        h  r  
        i  t  
        n  a  
        g  i  
           n  
           m  
           e  
           n  
           t  

```
