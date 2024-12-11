#!/usr/bin/python3

def is_prime(num):
    """Check if a number is a prime."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_prime_counts(n):
    """Generate a list of prime counts up to n."""
    primes = [0] * (n + 1)
    count = 0

    for i in range(1, n + 1):
        if is_prime(i):
            count += 1
        primes[i] = count

    return primes

def isWinner(x, nums):
    """Determine the winner of the prime game."""
    if not nums or x < 1:
        return None

    max_n = max(nums)
    prime_counts = generate_prime_counts(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
