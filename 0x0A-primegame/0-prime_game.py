#!/usr/bin/python3
"""0. Prime Game"""


def is_prime(n):
    """Check if n is prime"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def calculate_primes(n, primes):
    """Calculate primes"""
    for i in range(1, n + 1):
        if is_prime(i):
            primes.append(i)


def isWinner(x, nums):
    """Prime Game"""
    if not nums or x < 1:
        return None
    n = max(nums)
    primes = []
    calculate_primes(n, primes)
    primes_wins = 0
    for round in range(x):
        winner = 0
        for i in nums:
            if i in primes:
                winner += 1
        if winner % 2 == 0:
            primes_wins += 1
    if primes_wins * 2 == x:
        return None
    if primes_wins * 2 > x:
        return "Maria"
    return "Ben"
