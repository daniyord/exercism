def to_rna(dna_strand):
    list = []

    for letter in dna_strand:
        if letter == "C":
            list.append("G")
        if letter == "G":
            list.append("C")
        if letter == "T":
            list.append("A")
        if letter == "A":
            list.append("U")

    return "".join(list)
