#!/usr/bin/env python3
 # -*- coding: utf-8 -*-
"""
Created on Saturday,  September the 10th. 2022

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

@author: Jean-Yves Tinevez
"""


base = {
    0: '',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
    100: 'hundred'
}


def to_text_100(i, space):
    if i<=20:
        return base[i]
    if i<100:
        units = i % 10
        decades = i // 10
        if units == 0:
           space = ''
        hyphen = '-'
        if space == '':
           hyphen = ''
        return base[decades*10] + hyphen + base[units]

def to_text_1000(i, space):
    if i<100:
        return to_text_100(i, space)
    hundreds = i // 100
    remainder = i % 100
    if remainder == 0:
       return  base[hundreds] + space + 'hundred'
    return base[hundreds] + space + 'hundred' + space + 'and' + space + to_text_100(remainder, space)

def to_text(i, space=' '):
    if not isinstance(i, int):
        return 'Cannot transform numbers that are not integers'
    if i>=21000:
        return 'Cannot transform numbers larger than 20999'
    if i <=0:
        return 'Can only transform strictly positive integers'
    if i<1000:
        return to_text_1000(i, space)
    thousands = i // 1000
    remainder = i % 1000
    if remainder == 0:
        return base[thousands] + space + 'thousand'
    return base[thousands] + space + 'thousand' + space + to_text_1000(remainder, space)

total = 0
for i in range(1, 1001):
    text = to_text(i, '')
    print( ' - %5d -> %s' % (i, text ) )
    total = total + len(text)

print('total number of letters: %s' % total)

