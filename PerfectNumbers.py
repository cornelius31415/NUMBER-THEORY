#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:34:16 2024

@author: cornelius
import time

print("\n------------------------------------------------------------------------------------------")
print("                                  PERFECT NUMBERS                                  ")
print("------------------------------------------------------------------------------------------")
"""
                PERFECT NUMBERS
                
            A perfect number is the sum of its divisors.
            (including 1 and excluding itself)
            The first two perfect numbers are 6 and 28.
            
            This code contains a brute force algorithm to 
            calculate the first few perfect numbers and 
            a mathematical algorithm making use of Mersenne primes
            and the theorem Euler prooved.

"""

#------------------------------------------------------------------------------------------
#                                   BRUTE FORCE ALGORITHM 
#------------------------------------------------------------------------------------------

start = time.time()

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


print(f"\n  The first 4 perfect numbers are: {perfect_numbers(4)}")

end = time.time()
runtime = end-start
print(f"\n  Runtime Brute Force:              {runtime} s \n")

#------------------------------------------------------------------------------------------
#                                   MERSENNE PRIME ALGORITHM 
#------------------------------------------------------------------------------------------

start = time.time()

# checks if n is a prime
def is_prime(n):
    
    for i in range(2,int((n**0.5)+1)):
        if n % i == 0:
            return False
    
    return True


# generates a certain amount of mersenne primes
def mersenne_prim(amount):
    
    # Mersenne Primzahl: 2**k - 1 
    
    mersenne_primes = []
    
    k = 2
    while len(mersenne_primes) < amount:
        
        mersenne = (2 ** k) -1
        if is_prime(mersenne) == True:
            mersenne_primes.append((mersenne,k))
        
        k += 1
        
    
    return mersenne_primes


# generates a certain amount of perfect numbers
def perfekte_zahlen(amount):
    
    perfects = []
    mersennes = mersenne_prim(amount)
    
    for element in mersennes:
        k = element[1]
        mersenne = element[0]
        
        perfect = 2**(k-1)*mersenne
        perfects.append(perfect)
    
    return perfects
    
print("--------------------------------------------------------------------------------------------")
print("\n  The first 8 perfect numbers are: ",perfekte_zahlen(8),"\n")

end = time.time()
runtime = end-start
print("  Mersenne Prime Runtime:           ",runtime,"s")






