def triplets_with_sum(number):
    result = []

    for a in range(1, number + 1):
        for b in range(a + 1, number + 1):
            a2_b2 = a * a + b * b

            c = number - a - b

            if c < 0:
                break

            c2 = c ** 2

            if a2_b2 > c2:
                break

            if a2_b2 == c2:
                result.append([a, b, c])

    # print(result)
    return result


# triplets_with_sum(30000)
