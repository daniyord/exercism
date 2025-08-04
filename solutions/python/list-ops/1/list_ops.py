def append(list1, list2):
    result = []

    for item in list1:
        result.append(item)

    for item in list2:
        result.append(item)

    return result


def concat(lists):
    result = []

    for list in lists:
        for item in list:
            result.append(item)

    return result


def filter(function, list):
    result = []

    for item in list:
        if function(item):
            result.append(item)

    return result


def length(list):
    result = 0

    for item in list:
        result += 1

    return result


def map(function, list):
    result = []

    for item in list:
        result.append(function(item))

    return result


def foldl(function, list, initial):
    acc = initial
    for item in list:
        acc = function(acc, item)
    return acc


def foldr(function, list, initial):
    acc = initial
    for item in reversed(list):
        acc = function(acc, item)
    return acc


def reverse(list):
    result = []

    for item in list:
        result.insert(0, item)

    return result
