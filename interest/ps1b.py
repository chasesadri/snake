# -*- coding: utf-8 -*-
"""
Problem Set 1B: Saving, with a raise

Created on Fri Sep 18 13:41:21 2020

@author: chase

INSTRUCTIONS:
    See contents/assignments/ps1/MIT6_0001F16_ps1
    
PARAMETERS:
    (INT):
        total_cost: Cost of dream home - entered by user
        current_savings: amount saved thus far - Starts at $0
        annual_salary: Self explanatory - entered by user
    (INT/FLOAT):
        portion_down_payment: Portion of cost required for down - 0.25 or 25%
        r: Annual return rate (receive current_savings*r/12 per month) - 0.04 or 4%
        portion_saved: Portion of salary each month dedicated to saving for down - 0.1 or 10%
            - entered by user
        monthly_salary: savings will be increased by r and a % of monthly
        semi_annual_raise): Self-explanatory - entered by user
    
DESCRIPTION:
    Modify the solution to part A to include the following:
        1. User entered semi-annual salary raise FLOAT(semi_annual_raise)
        2. Increase salary by that percentage for 6 month intervals
    
"""

annual_salary = int(input('Enter your starting annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
    # above could be int or float, undetermined
total_cost = int(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))
current_savings = 0
portion_down_payment = 0.25
r = 0.04
months = 0

while current_savings < total_cost * portion_down_payment:
    current_savings += current_savings * r / 12
    current_savings += annual_salary / 12.0 * portion_saved
    months += 1
    if months % 6 == 0:
        annual_salary *= 1 + semi_annual_raise

print('Number of months:', months)