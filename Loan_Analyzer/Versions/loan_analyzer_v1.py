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
