def flatten(iterable):
    result = []

    for item in iterable:
        if hasattr(item, '__iter__'):
            result += flatten(item)
        elif item is not None:
            result.append(item)

    return result
