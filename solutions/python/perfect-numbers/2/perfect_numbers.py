def get_factors(number):
    primes = {1}

    for index in range(2, int(number / 2 + 1)):
        if number % index == 0:
            primes.add(index)

    return primes


def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number <= 0:
        raise ValueError(
            "Classification is only possible for positive integers.")

    if number == 1:
        return "deficient"

    sum = 0

    for divisor in get_factors(number):
        sum += divisor

    if sum < number:
        return "deficient"
    if sum > number:
        return "abundant"
    return "perfect"
