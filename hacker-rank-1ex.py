# EX 1: Maximum Perimeter Triangle

import math
import os
import random
import re
import sys

def maximumPerimeterTriangle(sticks):
    
    # I sort the array in descending order to make it easier to find the largest sides
    # - sort() is a built-in Python list method that arranges elements in ascending order by default
    # - The reverse=True parameter tells it to sort in descending order instead
    sticks.sort(reverse=True)
    
    # The basic condition for forming a non-degenerate triangle is that the sum of any two sides must be greater than the third side
    # Since we have sorted the array in descending order, it is sufficient to check that b + c > a (where a is the longest side), because:
    # - If b + c > a, then by default a + c > b and a + b > c (since "a" is the largest)

    # I Iterate through the array looking at 3 consecutive elements at a time. This guarantees me that:
    # - I can find the triangle with the maximum perimeter (since we start with the largest numbers)
    # - I can find the triangle with the maximum side (first requirement of the problem)
    # - Of those with the same maximum side, I can find the one with the largest minimum side (second request)

    # - len(sticks) gets the total length of our array
    # - I subtract 2 from it because I need to look at 3 elements at a time (the last valid index is n-1, so the last triplet starts at index n-3
    # --> Therefore we can only iterate up to n-2)
    # - range() generates a sequence of numbers from 0 up to (but not including) the given number
    for i in range(len(sticks) - 2):
        
        # I take 3 consecutive elements from the array and assign them to variables a, b, c (this makes the code more readable (a, b, c is clearer than sticks[i], sticks[i+1], sticks[i+2])
        # Because I sort in descending order: a is always the largest of the 3 numbers, b is the middle number, c is the smallest number
        a, b, c = sticks[i], sticks[i + 1], sticks[i + 2]
        
        # I verify if these sides can form a non-degenerate triangle
        # In a triangle, the sum of any two sides must be greater than the third side
        if b + c > a:
            
            # Once I have found a valid triangle, I return its sides in non-decreasing order using sorted()
            return sorted([a, b, c])
    
    # If no valid triangle is found, I return [-1]
    return [-1]