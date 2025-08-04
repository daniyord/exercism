def transform(legacy_data):
    result = {}

    for key, value in legacy_data.items():
        print(key, value)
        for letter in value:
            result[letter.lower()] = key

    return result
