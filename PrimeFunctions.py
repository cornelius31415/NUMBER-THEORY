#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 14:27:17 2024

@author: cornelius
"""

from math import sqrt, log
import matplotlib.pyplot as plt


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


# Count amount of primes <= n
def prime_counts(n):
    return len(primes(n))
    

# x/logx function (from prime number theorem)
def xlogx(x):
    return x/log(x)


# Calculate the n-th prime
def n_th_prime(n):

    primes = []
    i = 2 
    while len(primes)<n:
        if is_prime(i):
            primes.append(i)
        i+=1
        
    return primes[-1]


print(n_th_prime(12))

# ------------------------- VISUALIZATION -------------------------------

x = [i for i in range(2,5000)]
y1 = [prime_counts(i) for i in x]
y2 = [xlogx(i) for i in x]


plt.plot(x,y1,label='Prime Number Function')
plt.plot(x,y2,label='x/logx')
plt.title('Prime Number Function & x/logx')
plt.legend()