#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 23:37:08 2020

Euler Projet - Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

@author: Jean-Yves Tinevez
"""

def primes_below( end ):
    if end < 2:
        return []
    
    # Max possible numbers of prime numbers below end.
    lng = int( (end//2) - 1 )

    primes = [ True ] * lng  
    for i in range( int( lng**0.5 ) ):  
        if primes[i]:
            for j in range(2*i*(i + 3) + 3, lng, 2*i + 3):
                primes[j] = False  
    return [2] + [i*2 + 3 for i, j in enumerate(primes) if j]

# Main

limit = 2e6
primes = primes_below( limit )
sum_primes = sum( primes )

    
print( "\nSum of prime numbers below %d: %d." % (limit, sum_primes ) )
