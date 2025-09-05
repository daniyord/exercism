from functools import lru_cache
from itertools import combinations

PRICE = 8
DISCOUNTS = {1: 0, 2: 5, 3: 10, 4: 20, 5: 25}
INF = 10**18


def price_of_groups(size):
    return size * PRICE * (100 - DISCOUNTS[size])


def total(basket):

    @lru_cache(None)
    def helper(state):
        books = sorted(state)
        if not books:
            return 0

        best = INF
        unique_books = sorted(set(books))

        for size in range(1, len(unique_books) + 1):
            for group in combinations(unique_books, size):
                remaining = list(books)
                for b in group:
                    remaining.remove(b)
                cost = price_of_groups(size) + helper(tuple(sorted(remaining)))
                best = min(best, cost)
        return best

    return helper(tuple(basket))
