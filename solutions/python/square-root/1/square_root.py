def square_root(number):
    if number == 1:
        return 1

    for i in range(number):
        if i * i == number:
            return i
