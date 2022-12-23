#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 23:47:30 2022

@author: dan
"""
# all of these figures on approximations from when video was made 
private = 45000

# cost of education grows by 3% per year 

education_cost_increase_percentage = 1.03

year_one_of_education = private * education_cost_increase_percentage**18
print("The first year of education will be: $"+str(year_one_of_education))

year_two_of_education = private * education_cost_increase_percentage**19
print("The second year of education will be: $"+str(year_two_of_education))

year_three_of_education = private * education_cost_increase_percentage**20
print("The third year of education will be: $"+str(year_three_of_education))

year_four_of_education = private * education_cost_increase_percentage**21
print("The fourth year of education will be: $"+str(year_four_of_education))

total_tuition_cost = year_one_of_education + year_two_of_education + year_three_of_education + year_four_of_education 

print("The total tuition cost will be: $"+str(total_tuition_cost))

months_in_a_year = 12 
years_before_college = 18 

num_of_payments = months_in_a_year * years_before_college

print("The total number of payments will be: "+str(num_of_payments))

print("If you don't invest the money each payment will be : $"+str(total_tuition_cost/num_of_payments))


yearly_yield_if_payments_are_invested = .036
monthly_yield_if_payments_are_invested = 1+(yearly_yield_if_payments_are_invested / 12) 

payment_cost_if_invested = (total_tuition_cost*(monthly_yield_if_payments_are_invested-1))/((monthly_yield_if_payments_are_invested**num_of_payments)-1)


print("If you do invest the money each payment will be : $"+str(payment_cost_if_invested))

print("If you do invest the money, and your child will be going to public school each payment will be : $"+str(payment_cost_if_invested/2))



