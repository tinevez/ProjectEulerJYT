#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Factorial digit sum

Problem 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

Created on Sunday, September the 11th 2022
@author Jean-Yves Tinevez
'''

import math

a = math.factorial(100)
print('100! = %d' % a)
s = str(a)
sum = 0
for c in s:
    val = int(c)
    sum = sum + val

print('Sum of digits: %s' % sum)


