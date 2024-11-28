#!/usr/bin/python3
"""A function to determine the fewest number of coins needed
   to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Calculate the minimum number of coins required to meet a given total.
    
    Args:
        coins (list): A list of coin denominations.
        total (int): The total amount to achieve.

    Returns:
        int: The fewest number of coins needed, or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins = sorted(coins, reverse=True)
    counter = 0

    for coin in coins:
        if total <= 0:
            break
        # Use as many of this coin as possible
        counter += total // coin
        total %= coin

    # Check if we successfully met the total
    return counter if total == 0 else -1
