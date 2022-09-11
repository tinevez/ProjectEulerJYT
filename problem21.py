#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Amicable numbers
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

Created on Sunday, September the 11th 2022
@author Jean-Yves Tinevez
'''

divisors_dict = { 1: [] }

def proper_divisors(n):

    if n in divisors_dict:
        return divisors_dict[n]
    
    divs = set()
    # No need to start from more than the half.
    for i in range(n // 2, 0, -1):

        # Already tested?
        if i in divs:
            continue

        # Test.
        if n % i == 0:
            # i is a divisor
            divs.add(i)
            # all the divisors of i are also divisors or n
            divs.update( proper_divisors(i) )
    
    div_list = list(divs)
    div_list.sort()
    divisors_dict[n] = div_list
    return div_list

def d(n):
    return sum(proper_divisors(n))

total = 0
for i in range(1, 10000):
    ib = d(i)
    # print('sum of proper divisors: %d' % ib)
    dib = d(ib)
    # print('sum of proper divisors of sum of proper divisors: %d' % dib)
    if (dib == i) and (ib != i):
        print('- %5d and %5d are AMICABLE!' % (i, ib))
        total = total + i # apparently we only sum one of them.

print('\nSum of all amicable numbers under 10000: %d' % total)


