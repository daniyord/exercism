simple_operations = ["plus", "minus"]
complex_operations = ["multiplied", "divided"]


def answer(question):
    normalized_question = question[8:-1]

    if len(normalized_question) == 0:
        raise ValueError("syntax error")

    tokens = normalized_question.split(" ")

    # print(tokens)

    state = "operand1"
    expect_by = False

    op1 = None
    operation = None
    op2 = None

    for token in tokens:
        # print(state, token, op1, op2, operation)

        if state == "operand1":
            if token.lstrip("-").isdigit():
                op1 = int(token)
                state = "operation"
            elif token in simple_operations or token in complex_operations:
                raise ValueError("syntax error")
            else:
                raise ValueError("unknown operation")

        elif state == "operation":
            if token in simple_operations:
                operation = token
                state = "operand2"

            elif token in complex_operations:
                operation = token
                expect_by = True

            elif token == "by" and expect_by:
                expect_by = False
                state = "operand2"

            elif token.lstrip("-").isdigit():
                raise ValueError("syntax error")

            else:
                raise ValueError("unknown operation")

        elif state == "operand2":
            if token.lstrip("-").isdigit():
                op2 = int(token)
                op1 = calculate(op1, op2, operation)
                operation = None
                op2 = None
                state = "operation"
            else:
                raise ValueError("syntax error")

    if state == "operand2":
        raise ValueError("syntax error")
    else:
        return op1


def calculate(op1, op2, operation):
    if operation == "plus":
        return op1 + op2
    if operation == "minus":
        return op1 - op2
    if operation == "multiplied":
        return op1 * op2
    if operation == "divided":
        return op1 / op2
