def triplets_with_sum(number):
    result = []
    for a in range(1, number + 1):
        for b in range(a + 1, number + 1):
            c = number - a - b

            if c < 0:
                break

            a2_b2 = a * a + b * b
            c2 = c * c

            if a2_b2 > c2:
                break

            if a2_b2 == c2:
                result.append([a, b, c])

    return result
