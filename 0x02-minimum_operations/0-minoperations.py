#!/usr/bin/python3

"""
    A method that determines the number of minmum operations given n characters

"""


def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        # Check if n is divisible by factor
        while n % factor == 0:
            operations += factor  # Add the factor to operations
            n //= factor  # Reduce n by the factor
        factor += 1

    return operations
