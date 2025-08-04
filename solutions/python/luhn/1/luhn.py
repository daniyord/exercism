class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num
        pass

    def valid(self):
        self.card_num = self.card_num.replace(" ", "")

        if (len(self.card_num) <= 1):
            return False

        symbols = []

        for symbol in reversed(self.card_num):
            if not symbol.isdigit():
                return False
            symbols.append(int(symbol))

        for i in range(1, len(symbols), 2):
            new_value = symbols[i] * 2
            if new_value > 9:
                new_value = new_value - 9
            symbols[i] = new_value

        return sum(symbols) % 10 == 0
