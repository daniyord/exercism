def rotate(text, key):
    UPPERCASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LOWERCASE = 'abcdefghijklmnopqrstuvwxyz'
    UPPERCASE_SHIFTED = UPPERCASE[key:] + UPPERCASE[:key]
    LOWERCASE_SHIFTED = LOWERCASE[key:] + LOWERCASE[:key]

    return text.translate(str.maketrans(UPPERCASE+LOWERCASE, UPPERCASE_SHIFTED+LOWERCASE_SHIFTED))
