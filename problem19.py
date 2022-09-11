#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Created on Sunday, September the 11th 2022

Counting Sundays
Problem 19
You are given the following information, but you may prefer 
to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not 
on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the 
twentieth century (1 Jan 1901 to 31 Dec 2000)?

@author Jean-Yves Tinevez
'''


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False

def month_duration(month, year):
    if month == 2:
        if is_leap_year(year):
            return 29
        return 28

    if month == 9 or month == 4 or month == 6 or month == 11:
        return 30
    return 31

def increment_date(day, month, year):
    md = month_duration(month, year)
    day = day + 1
    if day > md:
        day = 1
        month = month + 1
        if month > 12:
            month = 1
            year = year + 1
    return (day, month, year)

next = {
    'Monday':       'Tuesday',
    'Tuesday':      'Wednesday',
    'Wednesday':    'Thursday',
    'Thursday':     'Friday',
    'Friday':       'Saturday',
    'Saturday':     'Sunday',
    'Sunday':       'Monday' }

def next_day(day_of_the_week):
    return next[day_of_the_week]

month_names = {
    1:  'January',
    2:  'February',
    3:  'March',
    4:  'April',
    5:  'May',
    6:  'June',
    7:  'July',
    8:  'August',
    9:  'September',
    10: 'October',
    11: 'November',
    12: 'December' }

# 1 Jan 1900
day = 1
month = 1 
year = 1900

day_of_the_week = 'Monday'

# Brute force

# First find the beginning of the century.
while True:
    (day, month, year) = increment_date(day, month, year)
    day_of_the_week = next_day(day_of_the_week)

    if day == 1 and month == 1 and year == 1901:
        break

print('The %d %s %d was a %s' % (day, month_names[month], year, day_of_the_week))

# Now iterates through the century.
n_sundays = 0
while True:
    (day, month, year) = increment_date(day, month, year)
    day_of_the_week = next_day(day_of_the_week)

    if day == 1 and day_of_the_week == 'Sunday':
        n_sundays = n_sundays + 1
        print('The %d %s %d was a %s' % (day, month_names[month], year, day_of_the_week))

    if day == 1 and month == 1 and year == 2001:
        break

print('Total number of Sundays falling on the 1st of the month in the 20th century: %s' % n_sundays)

