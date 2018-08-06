""" Lab 13: Final Review """

# Q1
# Old version
def count_change(amount, coins=(50, 25, 10, 5, 1)):
    """
    >>> count_change(7, (1, 2, 4, 8))
    6
    """
    if amount == 0:
        return 1
    elif amount < 0 or len(coins) == 0:
        return 0
    return count_change(amount, coins[1:]) + count_change(amount - coins[0], coins)

# Version 2.0
def make_count_change():
    """Return a function to efficiently count the number of ways to make
    change.

    >>> cc = make_count_change()
    >>> cc(500, (50, 25, 10, 5, 1))
    59576
    """
    computed = {}
    def count_change(amount, coins=(50, 25, 10, 5, 1)):
        if amount == 0:
            return 1
        elif amount < 0 or len(coins) == 0:
            return 0
        elif (amount, coins) in computed:
            return computed[(amount,coins)]
        else:
            count = count_change(amount, coins[1:]) + count_change(amount - coins[0], coins)
            computed[(amount, coins)] = count
            return count
    return count_change
