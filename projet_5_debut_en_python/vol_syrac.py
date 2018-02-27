#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""I believe I can fly..."""

import matplotlib.pyplot as plt

N = 1000000
DOT_FORMAT = "or"

def memoize(func):
    """Memoization decorator."""
    stored_results = {}

    def wrapper(*args):
        """Wrapper function."""
        if args in stored_results:
            return stored_results[args]
        else:
            result = func(*args)
            stored_results[args] = result
            return result

    return wrapper

def syracuse_height(n):
    """Computes fly height of syracuse(n)."""
    c = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        c += 1
    return c

@memoize
def syracuse_height_rec(n):
    """Computes fly height of syracuse(n)."""
    if n == 1:
        return 0
    else:
        if n % 2 == 0:
            return 1 + syracuse_height_rec(n // 2)
        else:
            return 1 + syracuse_height_rec(3 * n + 1)

def fly_graph(n):
    """Computes fly graph."""
    plt.figure()
    records = [0]
    for i in range(1, n + 1):
        records.append(syracuse_height(i))
    plt.axis([0, len(records) - 1, 0, max(records) + 1])
    plt.plot(range(len(records)), records, DOT_FORMAT)
    plt.show()

def fly_graph_rec(n):
    """Computes fly graph."""
    plt.figure()
    records = [0]
    for i in range(1, n + 1):
        records.append(syracuse_height_rec(i))
    plt.axis([0, len(records) - 1, 0, max(records) + 1])
    plt.plot(range(len(records)), records, DOT_FORMAT)
    plt.show()

def main():
    """Main function."""
    fly_graph_rec(N)

if __name__ == "__main__":
    main()
