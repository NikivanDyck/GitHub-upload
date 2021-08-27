# coding: utf-8
import csv
from os import add_dll_directory
from pathlib import Path
from typing import ValuesView



"""Part 1: Automate the Calculations"""
# Automate the calculations for the loan portfolio summaries.
# List of loan portfolio summaries. count loans, sum loans, calculate the average loan price. 
# Printing after each calculation 

loan_costs = [500, 600, 200, 1000, 450]

print("**Review of loan portfolio summaries")

#count
total_loans=len(loan_costs)
print(f"Count of all loans, {total_loans}")

#sum
all_loan_costs=sum(loan_costs)
print(f"Sum of all loan costs ${all_loan_costs: .2f}")

#average
average_loan_price=all_loan_costs/total_loans
print(f"Average loan amount ${average_loan_price: .2f}")



"""Part 2: Analyze Loan Data.​"""
#Analyze the loan to determine the investment evaluation.

print("**Investment evaluation of a single loan")

# Given loan data
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#Calulating future and remaining months 
#   **Future Value**: The amount of money the borrower has to pay back upon maturity of the loan (a.k.a. "Face Value")
#   **Remaining Months**: The remaining maturity (in months) before the loan needs to be fully repaid.
future_value=loan.get("future_value")
remaining_months=loan.get("remaining_months")

# Print Future Value and Remaining Months on the loan.
print(f"Future value ${future_value}")
print(f"Remaining months on loan {remaining_months}")

#Present Value to calculate a "fair value" of the loan.
#minimum required return of 20% as the discount rate.
#**monthly** version of the present value formula.
discount_rate=0.20
Present_Value = future_value / (1 + discount_rate/12) ** remaining_months
print(f"Fair value of loan ${Present_Value: .2F}")

#Present Value represents what the loan is really worth, does it make sense to buy the loan at its cost?
print("Does present loan value support purchasing?")

loan_price=loan.get("loan_price")
if Present_Value > loan_price:
    print("Yes - Buy now")
else: 
    print("No - Pass too expensive")



"""Part 3: Perform Financial Calculations of new loan"""
print("**Analysis of a new loan")

# Given the following loan data
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

#calculate present value.
#parameters for `future_value`, `remaining_months`, and the `annual_discount_rate`
#    The function should return the `present_value` for the loan.
def cal_present_value(future_value, remining_months, annual_discount_rate):
    present_value = future_value / (1 + annual_discount_rate/12) ** remaining_months   
    return present_value

#Calculate the new present value 
#Used an `annual_discount_rate` of 0.2 for this new loan calculation.
new_present_value= cal_present_value(new_loan.get("future_value"),new_loan.get("remaining_months"),0.20) 
print(f"The present value of the new loan is: {new_present_value: .2F}")


"""Part 4: Conditionally filter lists of loans."""
print("**List of inexpensive loans")

#provided loan list 
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# create empty list `inexpensive_loans`
inexpensive_loans = []


# add all the loans that cost $500 or less to the `inexpensive_loans` list
for current_loan in loans:
    loan_price = current_loan["loan_price"]
    
    if loan_price <= 500:
        inexpensive_loans.append(current_loan)



#Print the `inexpensive_loans` list

print(inexpensive_loans)



"""Part 5: Save the results."""
#printing inexspensive loan results

#header
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

#output file path
output_path = Path("inexpensive_loans.csv") 

#status
print ("Writing inexpensive loans list to CSV file")

#write to csv
with open(output_path,"w", newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(header)
    for item in inexpensive_loans:
        csvwriter.writerow(item.values())

csvfile.close()



"""Validation """
#verify if CSV reflects exspected results 
loan_count=len(inexpensive_loans)
print(f"Inexpensive loans csv contains a list of {loan_count} loans")




