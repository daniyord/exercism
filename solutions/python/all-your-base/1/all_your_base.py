def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    for digit in digits:
        if not 0 <= digit < input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    return from_10(to_10(input_base, digits), output_base)


def to_10(input_base, digits):
    result = 0

    deg = 0
    for digit in reversed(digits):
        if digit > 0:
            result += digit * (input_base ** deg)

        deg += 1

    return result


def from_10(input, output_base):
    if input == 0:
        return [0]

    result = []

    while input > 0:
        result.insert(0, input % output_base)
        input = input // output_base

    return result
