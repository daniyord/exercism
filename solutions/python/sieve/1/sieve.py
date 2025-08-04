def primes(limit: int):
    options = set()

    for number in range(2, limit + 1):
        options.add(number)

    for number in range(2, limit + 1):
        if number in options:
            for i in range(number + number, limit + 1, number):
                if i in options:
                    options.remove(i)

    return list(options)
