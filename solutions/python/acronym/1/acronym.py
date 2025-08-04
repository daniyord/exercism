def abbreviate(words):
    parts = words.replace("_", "").replace("-", " ").split(" ")

    result = []

    for part in parts:
        if len(part) > 0:
            result.append(part[0].upper())

    return "".join(result)
