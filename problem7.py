#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:07:22 2020

Euler Project - Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see 
that the 6th prime is 13.

What is the 10 001st prime number?

@author: Jean-Yves Tinevez
"""

# Global variable.
prime_numbers = [ 2, 3, 5, 7, 11, 13 ]

def is_prime( number ):
    for p in prime_numbers:
        if number % p == 0:
            return False        
    return True


n_pms = len( prime_numbers )
target_npms = 10001

while n_pms < target_npms:
    last_prime = prime_numbers[ -1 ]
    to_test = last_prime 
    
    while True:
        to_test = to_test + 2
        if is_prime( to_test ):
            prime_numbers.append( to_test )
            n_pms = len( prime_numbers )
            print( 'Found %dth ptime number: %d.' % ( n_pms, to_test ) )
            break
            
            
        
      