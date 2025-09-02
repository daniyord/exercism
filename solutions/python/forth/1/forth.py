import re


class StackUnderflowError(Exception):
    def __init__(self, message):
        self.message = message


def is_integer(input: str):
    int_pattern = re.compile(r"^[+-]?\d+$")
    return int_pattern.match(input)


def read_operands(result):
    if len(result) < 2:
        raise StackUnderflowError("Insufficient number of items in stack")

    return (result.pop(-2), result.pop(-1))


def read_operand(result):
    if len(result) < 1:
        raise StackUnderflowError("Insufficient number of items in stack")

    return result.pop(-1)


def evaluate_calculation(input_data: str, word_definitions: dict):
    for word_definition in word_definitions:
        input_data = input_data.replace(
            word_definition, word_definitions[word_definition]
        )

    tokens = input_data.split(" ")

    result = []

    for token in tokens:
        if is_integer(token):
            result.append(int(token))
        elif token == "-":
            op1, op2 = read_operands(result)
            result.append(op1 - op2)
        elif token == "+":
            op1, op2 = read_operands(result)
            result.append(op1 + op2)
        elif token == "/":
            op1, op2 = read_operands(result)

            if op2 == 0:
                raise ZeroDivisionError("divide by zero")

            result.append(op1 // op2)
        elif token == "*":
            op1, op2 = read_operands(result)
            result.append(op1 * op2)
        elif token == "dup":
            op = read_operand(result)
            result.append(op)
            result.append(op)
        elif token == "drop":
            op = read_operand(result)
        elif token == "swap":
            op1, op2 = read_operands(result)
            result.append(op2)
            result.append(op1)
        elif token == "over":
            op1, op2 = read_operands(result)
            result.append(op1)
            result.append(op2)
            result.append(op1)
        else:
            raise ValueError("undefined operation")

    return result


def evaluate_word_definition(input_data: str, word_definitions: dict):
    parts = input_data.split(" ")[1:-1]

    key = parts[0]

    if is_integer(key):
        raise ValueError("illegal operation")

    value = str.join(" ", parts[1:])

    for word_definition in word_definitions:
        value = value.replace(word_definition, word_definitions[word_definition])

    return {key: value}


def evaluate(input_data: list[str]):
    input_data = [x.lower() for x in input_data]
    calculation_data = input_data[-1]

    word_definitions = {}

    for input_part in input_data:
        if input_part.startswith(":"):
            word_definitions.update(
                evaluate_word_definition(input_part, word_definitions)
            )

    return evaluate_calculation(calculation_data, word_definitions)
