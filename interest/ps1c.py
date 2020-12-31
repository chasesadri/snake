# -*- coding: utf-8 -*-
"""
Problem Set 1C: Finding the right amount to save away

Created on Fri Sep 18 13:49:26 2020

@author: chase

INSTRUCTIONS:
    See contents/assignments/ps1/MIT6_0001F16_ps1
    
PARAMETERS:
    (INT):
        total_cost: Cost of dream home - $1M
        current_savings: amount saved thus far - Starts at $0
        annual_salary: Self explanatory - entered by user
    (INT/FLOAT):
        portion_down_payment: Portion of cost required for down - 0.25 or 25%
        r: Annual return rate (receive current_savings*r/12 per month) - 0.04 or 4%
        portion_saved: Portion of salary each month dedicated to saving for down - 0.1 or 10%
            - entered by user
        monthly_salary: savings will be increased by r and a % of monthly
        semi_annual_raise): Self-explanatory - 0.07 or 7%
    
DESCRIPTION:
    Similar to previous parts, we are attempting to determine how long it would take 
    to save for one's dream home. In this part however, we are trying to find HOW to save
    (best savings rate) for a given salary if we only have 36 months to save. Notifies
    user if it is not possible to save for the down payment in 36 months.

HINTS:
    We are searching for a float - limit to two decimals of accuracy (save 7.04% or 0.0704)
        -> Search for an int 0-10000 then convert to decimal
    Bisection search could work
        
"""

annual_salary = int(input('Enter your starting annual salary: '))
total_cost = 1000000
semi_annual_raise = 0.07
current_savings = 0
portion_down_payment = 0.25
r = 0.04
new_salary = annual_salary
epsilon = 100
months = 0
steps = 0

# Bisection Approach
low_rate = 0
high_rate = 10000

for months in range(36):
    if months % 6 == 0 and months != 0:
        new_salary *= 1 + semi_annual_raise
    current_savings += current_savings * r / 12
    current_savings += new_salary / 12.0 * (high_rate / 10000.0)
    
if current_savings < total_cost * portion_down_payment:
    print('No way to afford in 3 years :\'(')
else:
    while abs(current_savings - (total_cost * portion_down_payment)) >= epsilon:
        land = int((low_rate + high_rate) / 2)
        current_savings = 0
        new_salary = annual_salary
        for months in range(36):
            if months % 6 == 0 and months != 0:
                new_salary *= 1 + semi_annual_raise
            current_savings += current_savings * r / 12
            current_savings += new_salary / 12 * (land / 10000)
        if total_cost * portion_down_payment > current_savings:
            low_rate = land
        else:
            high_rate = land
        steps += 1
    print('Best savings rate:', land / 10000)
    print('Steps in search:', steps)