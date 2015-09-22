import timeit
from math import sqrt

__author__ = 'Jean-Yves'

"""
Largest palindrome product
Problem 4
A palindromic number reads the same both ways. The
largest palindrome made from the product of two 2-digit
numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def largest_palindrome():
    """
    The largest number made of the product of two 3-digits numbers
    is 998001. It has 6 digits. So we build palindrome numbers
    starting from this one and going down, and check whether the
    palindrome we engineered is the product of two 3-digits numbers.
    """

    seed = 997
    # Will generate 997799, which is the first palindrome below 998001.
    while seed >= 100:
        s = str(seed)
        ls = s + s[::-1]
        p = int(ls)
        a = 999
        while a > sqrt(p):
            if p % a == 0:
                # We found it!
                return [p, a, p/a]
            a -= 1

        # This palindrome is not good. Loop
        seed -= 1


start_time = timeit.default_timer()
[pl, al, bl] = largest_palindrome()
elapsed = timeit.default_timer() - start_time

print('Largest palindrome product of two 3-digits numbers is %d = %d x %d.' % (pl, al, bl) )
print('Computation took %f ms' % (1000*elapsed))
