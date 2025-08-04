def factors(value):
    result = []

    num = 1
    while value > 1:
        num += 1
        while value % num == 0:
            result.append(num)
            value = value // num

    return result
