#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 23:35:56 2020


Project Euler - Problem 13.
Longest Collatz sequence

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 
10 terms. Although it has not been proved yet (Collatz Problem), it is thought 
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.


@author: Jean-Yves Tinevez
"""
import time


# Global variable.
# Maps the start of a sequence to the length of this sequence.
collatz_dict = {}
# Initialize it.
collatz_dict[ 1 ] = 1


def next_collatz( n ):
    if n % 2 == 0:
        return n/2
    else:
        return 3 * n + 1
    
def collatz_sequence_length( start ):
    
    length = 1
    n = start
    while n != 1:
        
        n = next_collatz( n )
        if n in collatz_dict:
            length += collatz_dict[ n ]
            collatz_dict[ start ] = length
            return
        
        length += 1


#__________________________________________________________________
n_max = 1000000

t1 = time.perf_counter()

for start in range( 1, n_max ):
        collatz_sequence_length( start )

t2 = time.perf_counter()

max_key = max( collatz_dict, key = collatz_dict.get)
print( 'Longest Collatz sequence below %d is %d for start = %d.'\
      % ( n_max, collatz_dict[ max_key ], max_key ) )
print( 'Done in %.1f s.' % ( t2-t1 ) )
