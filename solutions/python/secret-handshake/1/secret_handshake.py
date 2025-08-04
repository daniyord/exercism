def commands(binary_str):
    code_parts = []

    if binary_str[4] == "1":
        code_parts.append("wink")

    if binary_str[3] == "1":
        code_parts.append("double blink")

    if binary_str[2] == "1":
        code_parts.append("close your eyes")

    if binary_str[1] == "1":
        code_parts.append("jump")

    if binary_str[0] == "1":
        code_parts.reverse()

    return code_parts
