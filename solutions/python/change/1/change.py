def find_fewest_coins(coins, target):
    results = []

    for coin in reversed(coins):
        if coin <= target:
            find_fewest_coins1(coins, target - coin, [coin], results)

    return results[0] if len(results) > 0 else []


def find_fewest_coins1(coins, target, found, results):
    print(found, target)
    if len(results) > 0 and len(results[0]) < len(found):
        return

    if target == 0:
        current = results.pop() if len(results) > 0 else None

        found.sort()
        if current is None or len(found) < len(current):
            results.append(found)
        else:
            results.append(current)
        return

    for coin in reversed(coins):
        if coin <= target and coin <= min(found):
            find_fewest_coins1(coins, target - coin, found + [coin], results)


# result = find_fewest_coins([1, 5, 10, 25], 1)
found = find_fewest_coins([1, 5, 10, 21, 25], 0)

# print(results)


print(found)
