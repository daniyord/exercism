def decimal_to_binary(number):
    bits = []
    while number > 0:
        bits.insert(0, number % 2)
        number = number // 2

    for i in range(0, 8 - len(bits)):
        bits.insert(0, 0)

    return bits


def binary_to_decimal(bits):
    result = 0
    for index, bit in enumerate(reversed(bits)):
        result += bit * 2 ** index
    return result


def encode_single(number):

    if number <= 127:
        return [number]

    bits = decimal_to_binary(number)

    result = []

    group = []
    first_group = True
    for index, bit in enumerate(reversed(bits)):
        group.insert(0, bit)

        if index == len(bits) - 1:
            for i in range(0, 7 - len(group)):
                group.insert(0, 0)

        if len(group) == 7:
            if first_group:
                group.insert(0, 0)
                first_group = False
            else:
                group.insert(0, 1)
            result.insert(0, group.copy())
            group = []

    return [binary_to_decimal(x) for x in result]


def encode(numbers):
    result = []
    for number in numbers:
        result += encode_single(number)

    return result


def decode(bytes):
    result = []

    group = []
    is_first = True
    for byte in reversed(bytes):
        bits = decimal_to_binary(byte)

        if bits[0] == 0 and not is_first:
            result.insert(0, binary_to_decimal(group))
            group = []

        if is_first:
            is_first = False
            if bits[0] != 0:
                raise ValueError("incomplete sequence")

        group = bits[1:] + group

    result.insert(0, binary_to_decimal(group))

    return result
