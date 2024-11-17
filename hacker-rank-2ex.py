# EX 2: Mark and Toys

import math
import os
import random
import re
import sys

# This is an optimisation problem where you have to find the maximum number of toys Mark can buy on a limited budget.
# - To maximise the number of toys, it is best to buy the cheapest ones first
# - So I have to sort the array of prices in ascending order
# - Then I add up the prices one by one until I exceed the budget
# - The number of toys I can add before exceeding the budget is the final result

def maximumToys(prices, k):
    # I sort the prices in ascending order to buy the cheapest toys first
    prices.sort()
    
    # I initialize variables to keep track of toys and spending:
    
    # toys_count keeps track of the number of toys we can buy
    toys_count = 0
    
    # total_spent keeps track of how much we spend
    total_spent = 0
    
    # I iterate through the sorted prices
    for price in prices:
        
        # I check if I can afford this toy
        # that is, I check whether by adding the price of the current toy I exceed the budget
        if total_spent + price <= k:
            
            # If I don't exceed it, I add the price to the total and increase the counter
            total_spent += price
            
            toys_count += 1
        
        else:
            
            # If I exceed it, I go out of the cycle because I can no longer buy toys
            break
            
    return toys_count