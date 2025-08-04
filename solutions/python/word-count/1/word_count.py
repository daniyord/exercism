def count_words(sentence):
    sentence = sentence.strip("'")

    delimiters = "\n\t:!?,@$%^&_."

    for delimiter in delimiters:
        sentence = sentence.replace(delimiter, ' ')

    parts = sentence.split()

    result = {}

    for part in parts:
        part = part.strip("'").lower()
        count = result.get(part, 0)
        count += 1
        result[part] = count

    return result
