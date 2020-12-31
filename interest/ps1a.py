# -*- coding: utf-8 -*-
"""
Problem Set 1A: House Hunting

Created on Fri Sep 18 13:15:12 2020

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
    
DESCRIPTION:
    Takes some user entered vales and determines how long it would take to save enough to make
    a down payment on a home.
    
"""

annual_salary = int(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
    # above could be int or float, undetermined
total_cost = int(input('Enter the cost of your dream home: '))
current_savings = 0
portion_down_payment = 0.25
r = 0.04
months = 0

while current_savings < total_cost * portion_down_payment:
    current_savings += current_savings * r / 12
    current_savings += annual_salary / 12.0 * portion_saved
    months += 1

print('Number of months:', months)