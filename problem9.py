#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from math import sqrt

"""
Created on Wed Mar 25 23:43:24 2020


Euler Project - Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.


@author: Jean-Yves Tinevez
"""

sum_triplet = 1000

for a in range( 1, sum_triplet // 2 ):
    for b in range( a + 1, sum_triplet ):
        term = sum_triplet**2 + 2 * a * b - 2 * (a+b) * sum_triplet
        if term == 0:
            c = int( sqrt( a**2 + b**2 ) )
            print('Found a Pythagorean triplet: ( %d, %d, %d) with sum = %d '\
                  'and product  = %d.' % ( a, b, c, a+b+c, a*b*c ) )


