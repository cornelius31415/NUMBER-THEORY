#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:34:16 2024

@author: cornelius
"""

"""
                PERFECT NUMBERS
                
            A perfect number is the sum of its divisors.
            (including 1 and excluding itself)
            The first two perfect numbers are 6 and 28.

"""


# checks if a number is perfect
def is_perfect(n):
    
    divisors = []
    for i in range(1,n):
        if n%i == 0:
            divisors.append(i)
    
    divisor_sum = sum(divisors)
    
    if divisor_sum == n:
        return True
    else:
        return False
    
 

print(is_perfect(28))


# creates a list of the first n perfect numbers
# (already takes an eternity fot n=5)
def perfect_numbers(n): 
    

    perfects = []
    i = 1
    while len(perfects)<n:
        if is_perfect(i):
            perfects.append(i)
        i += 1

    return perfects

print(perfect_numbers(4))

