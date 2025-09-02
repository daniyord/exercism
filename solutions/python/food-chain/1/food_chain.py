TEXTS = {
    "fly" : ("I don't know why she swallowed the fly. Perhaps she'll die.", None),
    "spider": ("She swallowed the spider to catch the fly.", "It wriggled and jiggled and tickled inside her."),
    "bird": ("She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.", "How absurd to swallow a bird!"),
    "cat": ("She swallowed the cat to catch the bird.", "Imagine that, to swallow a cat!"),
    "dog": ("She swallowed the dog to catch the cat.", "What a hog, to swallow a dog!"),
    "goat": ("She swallowed the goat to catch the dog.", "Just opened her throat and swallowed a goat!"),
    "cow": ("She swallowed the cow to catch the goat.", "I don't know how she swallowed a cow!"),
    "horse": ("She's dead, of course!", None)
}

RECITES = [
    ["fly"],
    ["spider", "fly"],
    ["bird", "spider", "fly"],
    ["cat", "bird", "spider", "fly"],
    ["dog", "cat", "bird", "spider", "fly"],
    ["goat", "dog", "cat", "bird", "spider", "fly"],
    ["cow", "goat", "dog", "cat", "bird", "spider", "fly"],
    ["horse"]
]

def list_join(delimiter, lists):
    result = []
    for i, lst in enumerate(lists):
        if i > 0:
            result += delimiter
        result += lst
    return result

def generate_verse(verse):
    result = []

    first = verse[0]

    result.append(f"I know an old lady who swallowed a {first}.",)

    if TEXTS[first][1] is not None:
        result.append(TEXTS[first][1])

    for verse_item in verse:
        result.append(TEXTS[verse_item][0])

    return result

def recite(start_verse, end_verse):
    result = []
    
    for verse in range(start_verse - 1, end_verse):
        result.append(generate_verse(RECITES[verse]))

    final_result = list_join([""], result)

    # print(*final_result, sep="\n")   

    return final_result
