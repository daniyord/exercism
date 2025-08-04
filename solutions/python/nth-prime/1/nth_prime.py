def prime(number):

    if number == 0:
        raise ValueError('there is no zeroth prime')

    current_number = 2
    while number > 0:
        if is_prime(current_number):
            number -= 1

        if number > 0:
            current_number += 1

    return current_number


def is_prime(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True
