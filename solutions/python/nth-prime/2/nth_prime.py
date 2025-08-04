def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')

    primes = [2]
    current_number = 2

    while len(primes) < number:
        current_number += 1
        if is_prime(current_number, primes):
            primes.append(current_number)

    return primes[-1]


def is_prime(number, primes):
    for prime in primes:
        if number % prime == 0:
            return False
    return True
