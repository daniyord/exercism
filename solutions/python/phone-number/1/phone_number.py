from string import ascii_letters


class PhoneNumber:
    def __init__(self, number):
        symbols_to_remove = "() +-."
        invalid_symbols = "@:!"

        for symbol_to_remove in symbols_to_remove:
            number = number.replace(symbol_to_remove, "")

        for symbol in number:
            if symbol in ascii_letters:
                raise ValueError("letters not permitted")
            if symbol in invalid_symbols:
                raise ValueError("punctuations not permitted")

        if len(number) == 11:
            if number[0] == "1":
                number = number[1:]
            else:
                raise ValueError("11 digits must start with 1")

        if len(number) < 10:
            raise ValueError("must not be fewer than 10 digits")

        if len(number) > 11:
            raise ValueError("must not be greater than 11 digits")

        if number[0] == "0":
            raise ValueError("area code cannot start with zero")

        if number[0] == "1":
            raise ValueError("area code cannot start with one")

        if number[3] == "0":
            raise ValueError("exchange code cannot start with zero")

        if number[3] == "1":
            raise ValueError("exchange code cannot start with one")

        self.number = number
        self.area_code = number[0:3]

    def pretty(self):
        return f"({self.number[0:3]})-{self.number[3:6]}-{self.number[6:]}"
