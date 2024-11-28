#!/usr/bin/python3
"""
Module for solving the change-making problem.
"""

def makeChange(coins, total):
    """
    Determine the minimum number of coins needed to meet a given total.
    Args:
        coins (list): The denominations of the coins.
        total (int): The total amount to achieve.
    Returns:
        int: The minimum number of coins, or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0
    
    # Sort coins in descending order
    coins.sort(reverse=True)
    num_coins = 0
    
    for coin in coins:
        if total == 0:
            break
        # Use as many of this coin as possible
        num_coins += total // coin
        total %= coin
    
    return num_coins if total == 0 else -1
