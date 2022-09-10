#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 23:42:28 2020


2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

@author: Jean-Yves Tinevez
"""

# Write the number on base 2. Easy.
bits = '1' + 1000 * '0'

# Convert it to decimal integer.
val = int( bits, 2 )

str_val = str( val )
sum_digits = 0
for s in str_val:
    sum_digits += int( s )
    
print( sum_digits )

