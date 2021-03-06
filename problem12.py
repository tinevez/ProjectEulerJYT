#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  5 23:23:13 2020

Project Euler - Problem 12.

The sequence of triangle numbers is generated by adding the natural numbers. 
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first 
ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred 
divisors?

--------------------------------------------------------

My approach: 
    - We can compute directly the next triangle number val.
    - This number has a prime decomposition p^a x q^b r^c ...
    - So the number of divisors is (a+1)(b+1)(c+1) ....

There is an optimization I missed:
    - val = n * (n+1) / 2
    - But n and (n+1) are coprimes (proof elsewhere).
    - So they do not have any common divisor.
    - So we can count the number of divisors separately on smaller numbers.
    We need to compute the number of divisors for:
        - n/2 and (n+1) if n is even;
        - (n+1)/2 and n if n is odd,
    and sum them.
    With this we deal with numbers that are smaller, requiring smaller 
    computation. And we can reuse (n+1) for the next iteration. 

@author: Jean-Yves Tinevez
"""

from math import floor, sqrt
import collections


# Croft Spiral sieve on floating point number, taken from 
# https://rosettacode.org/wiki/Prime_decomposition#Python
def factorize( n ):
    step = lambda x: 1 + (x<<2) - ((x>>1)<<1)
    maxq = int( floor( sqrt( n ) ) )
    d = 1
    q = 2 if n % 2 == 0 else 3 
    while q <= maxq and n % q != 0:
        q = step(d)
        d += 1
    return [q] + factorize(n // q) if q <= maxq else [n]



#____________________________________________________________

# Index of the triangle number.
n = 1 

limit = 500

while True:
    n += 1
    
    # Value of the ith triangle number.
    val = n * ( n + 1 ) // 2    

    # Decompose val over prime numbers.
    factors = factorize( val )
    
    # Count the divisors from the exponents of this decomposition.
    counter = collections.Counter( factors )
    n_divisors = 1 
    for exp in counter.values():
        n_divisors *= ( exp + 1 )    
        
    if (n_divisors > limit):
        print('For the %dth triangle number, %d, found %d divisors.' % \
              ( n, val, n_divisors ) )
        break
