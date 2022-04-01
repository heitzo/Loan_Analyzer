# coding: utf-8
import csv
import pathlib 
from pathlib import Path 


# """Part 1: Automate the Calculations.

# Automate the calculations for the loan portfolio summaries.

# First, let's start with some calculations on a list of prices for 5 loans.
#     1. Use the `len` function to calculate the total number of loans in the list.
#     2. Use the `sum` function to calculate the total of all loans in the list.
#     3. Using the sum of all loans and the total number of loans, calculate the average loan price.
#     4. Print all calculations with descriptive messages.
# """
loan_costs = [500, 600, 200, 1000, 450]

# Show how many loans are in the list
# Use the `len` function to calculate the total number of loans in the list.
number_of_loans = len(loan_costs)
print('The total number of loans in the portfolio is', number_of_loans)
# Print the number of loans from the list


# Find the total of all loans
# Use the `sum` function to calculate the total of all loans in the list.
total_loan_amount = sum(loan_costs)
print('the total of all loans is $', total_loan_amount)
# Print the total value of the loans

# What is the average loan amount from the list?
# Using the sum of all loans and the total number of loans, calculate the average loan price.
# define a variable 'average_loan_amount' 
average_loan_amount = (total_loan_amount) / (number_of_loans)
print('The average loan amount is $', average_loan_amount)
# Print the average loan amount


"""Part 2: Analyze Loan Data.

Analyze the loan to determine the investment evaluation.

Using more detailed data on one of these loans, follow these steps to calculate a Present Value, or a "fair price" for what this loan would be worth.

1. Use get() on the dictionary of additional information to extract the **Future Value** and **Remaining Months** on the loan.
    a. Save these values as variables called `future_value` and `remaining_months`.
    b. Print each variable.

    @NOTE:
    **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
    **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.

2. Use the formula for Present Value to calculate a "fair value" of the loan. Use a minimum required return of 20% as the discount rate.
3. Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
    a. If the present value of the loan is greater than or equal to the cost, then print a message that says the loan is worth at least the cost to buy it.
    b. Else, the present value of the loan is less than the loan cost, then print a message that says that the loan is too expensive and not worth the price.

    @NOTE:
    If Present Value represents the loan's fair value (given the required minimum return of 20%), does it make sense to buy the loan at its current cost?
"""

# Given the following loan data, you will need to calculate the present value for the loan
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Use get() on the dictionary of additional information to extract the Future Value and Remaining Months on the loan.
future_value = loan.get('future_value')
print('The future value of the loan is $',future_value)
# prints the future value of the loan

# define the remaining months 
remaining_months = loan.get("remaining_months")
print('The remaining time is', remaining_months, "months")
# print the remaining time

# define a new variable for loan price and pull the value from the loan'
loan_price = loan.get("loan_price")
print('The price of this loan is $', loan_price)
# print the price of loan

# calculate a "fair value" of the loan
# required return of 20% as the discount rate.
# Use the **monthly** version of the present value formula because the time period is in months
fair_value = (future_value) / ((1 + 0.20/12)**remaining_months)
# Present Value = Future Value / (1 + Discount_Rate/12) ** remaining_months
print("The present value of the loan is $", round(fair_value,2))

# If Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
# Write a conditional statement (an if-else statement) to decide if the present value represents the loan's fair value.
if fair_value >= loan_price:
    # If the present value of the loan is greater than or equal to the cost, 
    print("The loan is worth at least the cost to buy it.")
    # prints message that says the loan is worth at least the cost to buy it
elif fair_value < loan_price:
    #Else, the present value of the loan is less than the loan cost,
    print('The cost of the loan is too high, it is not worth buying')
    # prints a message that says that the loan is too expensive and not worth the price.

