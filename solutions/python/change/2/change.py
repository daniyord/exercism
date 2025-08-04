def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")

    if target == 0:
        return []

    result = []

    for coin in reversed(coins):
        if coin <= target:
            find_fewest_coins1(coins, target - coin, [coin], result)

    if len(result) > 0:
        return result
    else:
        raise ValueError("can't make target with given coins")


def find_fewest_coins1(coins, target, found, result):
    if len(result) > 0 and len(result) <= len(found):
        return

    if target == 0:
        found.sort()
        result.clear()
        result += found
        return

    for coin in reversed(coins):

        if coin <= target and coin <= found[-1]:
            find_fewest_coins1(coins, target - coin, found + [coin], result)
