def sum_of_multiples(level: int, items: list[int]) -> int:
    scores = set()

    for item in items:
        if item == 0:
            continue

        current = item
        while current < level:
            scores.add(current)
            current += item

    return sum(scores)
