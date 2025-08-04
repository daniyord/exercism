def transpose(text):
    max = 0
    lines = []

    matrix = []

    for line in text.split("\n"):
        lines.append(line)

        if len(line) > max:
            max = len(line)

    for index in range(0, max):
        matrix.append("")

    for line in lines:
        print(line)

        index = 0
        for symbol in line:
            matrix[index] += symbol
            index += 1

        for i in range(index, max):
            matrix[i] += " "

    for index, row in enumerate(matrix):
        matrix[index] = row.trim

    print(matrix)

    result = "\n".join(matrix)

    return result

    # text = "The first line.\nThe second line."
    # expected = "TT\nhh\nee\n  \nfs\nie\nrc\nso\ntn\n d\nl \nil\nni\nen\n.e\n ."


transpose("The longest line.\nA long line.\nA longer line.\nA line.")

# ['TAAA', 'h   ', 'elll', ' ooi', 'lnnn', 'ogge', 'n e.', 'glr', 'ei ', 'snl', 'tei', ' .n', 'le', 'i.', 'n', 'e', '.']
# "TAAA\nh   \nelll\n ooi\nlnnn\nogge\nn e.\nglr\nei \nsnl\ntei\n .n\nl e\ni .\nn\ne\n."
