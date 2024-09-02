#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:14:04 2024

@author: cornelius
"""


'''

                MÖBIUS FUNCTION
        
        - take prime factorization of a number n
        - if one of the prime factors has a power
          bigger than 1, the value of the Möbius function
          is 0
        - if the amount of prime factors is even then the
          Möbius function has a value of 1
        - if the amount of prime factors is odd, it is -1


'''

from math import sqrt, log
import matplotlib.pyplot as plt

print()

"""
-------------------------------------------------------------------------------
                            BASIC PRIME FUNCTIONS
-------------------------------------------------------------------------------
"""


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

primes = primes(1000) # list of primes smaller than 1000 


"""
-------------------------------------------------------------------------------
                            PRIME FACTORIZATION
-------------------------------------------------------------------------------
"""

    
# prime factors and how often they appear in the factorization
def factorization(n):
    
    factors = []
    num = n
    while num != 1:
        for factor in primes:
            if num % factor == 0:
                factors.append(factor)
                num = num/factor
    
            
    return sorted(factors)
            


n = 3*3*3*11*11*13
print(factorization(n))
    

"""
-------------------------------------------------------------------------------
                            MÖBIUS FUNCTION
-------------------------------------------------------------------------------
"""


def moebius(n):
    
    # when möbius = 0
    if len(list(set(factorization(n)))) != len(factorization(n)):
        return 0
    elif len(factorization(n))%2 == 0:
        return 1
    else:
        return -1
    
"""
-------------------------------------------------------------------------------
                            MÖBIUS FUNCTION
-------------------------------------------------------------------------------
"""

    
x = list(range(1,1000))
y = [moebius(i) for i in x]
plt.yticks([-1,0,1])
plt.xlabel("Number")

plt.title("Möbius Function")

plt.plot(x,y)






























