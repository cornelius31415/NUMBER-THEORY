#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:30:18 2024

@author: cornelius
"""

from math import sqrt, log



# prime numbers only divisible by 1 and themselves
# Check if a number is prime

def is_prime(n):
    
    for i in range(2,int(sqrt(n)+1)):
        if n % i == 0:
            return False
        
    return True


# Create a list of all primes <= n

def primes(n):
    
    primes = [i for i in range(2,n+1) if is_prime(i)]

    return primes


primes = primes(100)


"""
    The following function finds the prime factors of a 
    given number n
    The power of each prime factor is neglected
    So the prime factors of 12 will be 2 and 3 neglecting
    that 2 has a power of 2 -> 12 = 2 * 2 * 3
"""
def prime_factors(n):
    
    factors = []
    
    for prime in primes:
        if n % prime == 0:
            factors.append(prime)
            
    return factors 
        
print(prime_factors(12))

