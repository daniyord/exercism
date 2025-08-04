def is_anagram(word, candidate):
    word = word.lower()
    candidate = candidate.lower()

    if word == candidate:
        return False

    word_symbols = list(word)
    candidate_symbols = list(candidate)

    if len(word_symbols) != len(candidate_symbols):
        return False

    word_symbols.sort()
    candidate_symbols.sort()

    for index, symbol in enumerate(word_symbols):
        if symbol != candidate_symbols[index]:
            return False

    return True


def find_anagrams(word, candidates):
    result = []

    for candidate in candidates:
        if is_anagram(word, candidate):
            result.append(candidate)

    return result
