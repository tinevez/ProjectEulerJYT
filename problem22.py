#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Names scores
Problem 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand 
first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for 
each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 
3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
 So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

Created on Sunday, September the 11th 2022
@author Jean-Yves Tinevez
'''

names = []
with open('p022_names.txt') as file:
    for f in file:
        tokens = f.split(',')
        for t in tokens:
            names.append(t.replace('"', ''))
names.sort()

total_score = 0
for i in range(len(names)):
    name = names[i]
    alphabetical_value = 0
    for c in name:
        val = ord(c) - ord('A') + 1
        alphabetical_value = alphabetical_value + val
    score = (i+1) * alphabetical_value
    total_score = total_score + score
    if name == 'COLIN':
        print(' - %15s: %d' % (name, score))
        print(i)
        print(alphabetical_value)

print('\nTotal score: %d' % total_score)
