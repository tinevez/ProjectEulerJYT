#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Non-abundant sums
Problem 23

A perfect number is a number for which the sum of its proper divisors is exactly
equal to the number. For example, the sum of the proper divisors of 28 would be 
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less 
than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number 
that can be written as the sum of two abundant numbers is 24. By mathematical analysis, 
it can be shown that all integers greater than 28123 can be written as the sum of two 
abundant numbers. However, this upper limit cannot be reduced any further by analysis
even though it is known that the greatest number that cannot be expressed as the sum
of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of 
two abundant numbers.

Created on Sunday, October the 17th 2022
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

max = 28123 
# max = 400

print('Finding abundant numbers.')
# Set of all abundent numbers, below 28123-12.
abundant_number = []
for n in range(12, max+1):
    if d(n) > n:
        abundant_number.append(n)

print('Found %d abundant numbers.' % len(abundant_number))
# for d in abundant_number:
#     print(d)

print('Finding integers that cannot be expressed as the sum of 2 abundant numbers.')
not_sum_abundants = set(range(1, max+1))
for n1 in abundant_number:
    for n2 in abundant_number:
        if n1 + n2 <= max:
            if (n1+n2) in not_sum_abundants:
                not_sum_abundants.remove(n1+n2)
        else:
            break

print('Found %d such numbers.' % len(not_sum_abundants))
print('Their sum is: %d' % sum(not_sum_abundants))
