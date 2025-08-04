def is_vowel(char):
    return char in "aeiou"


def translate_word(word: str):
    if is_vowel(word[0]) or word.startswith("xr") or word.startswith("yt"):
        return f"{word}ay"

    if word.startswith("y"):
        return f"{word[1:]}{word[:1]}ay"

    for i in range(0, len(word)):
        if is_vowel(word[i:][0]) or word[i:][0] == "y":
            return f"{word[i:]}{word[:i]}ay"

        if word[i:].startswith("qu"):
            return f"{word[i+2:]}{word[:i+2]}ay"

    return word


def translate(text: str):
    words = text.split(" ")

    result = ""
    for word in words:
        result += f"{translate_word(word)} "

    return result.strip()
