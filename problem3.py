import timeit
from math import sqrt

__author__ = 'Jean-Yves'

"""
Largest prime factor
====================

Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


def largest_prime_factor(n):
    a = n
    if a % 2 == 0:
        a /= 2

    p = 3
    while True:
        if a % p == 0:
            a /= p
            continue
        else:
            p += 2

        if a < p:
            p -= 2
            return p


def largest_prime_factor2(n):
    a = n
    if a % 2 == 0:
        a /= 2

    p = 3
    last_factor = p
    max_factor = sqrt(n)
    while a > 1 & p <= max_factor:
        if a % p == 0:
            a /= p
            last_factor = p
            while a % p == 0:
                a /= p
            max_factor = sqrt(a)
            continue
        else:
            p += 2

    if a < p:
        return p
    else:
        return last_factor


start_time = timeit.default_timer()
val = largest_prime_factor(600851475143)
elapsed = timeit.default_timer() - start_time

print('Standard loop')
print('Largest prime factor of 600851475143 is %d.' % val )
print('Computation took %f ms' % (1000*elapsed))

start_time = timeit.default_timer()
val = largest_prime_factor2(600851475143)
elapsed = timeit.default_timer() - start_time

print('\nSquare-root loop')
print('Largest prime factor of 600851475143 is %d.' % val )
print('Computation took %f ms' % (1000*elapsed))
