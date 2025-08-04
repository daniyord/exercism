def factors(value):
    result = []

    for i in range(2, value + 1):
        if value == 1:
            break

        while value % i == 0:
            result.append(i)
            value = value // i

    return result
