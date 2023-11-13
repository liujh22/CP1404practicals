# this is a collection of words of nice words this is a fun thing it is
WORDS_TO_COUNT = {}
text = input("Text: ").split()

for words in text:
    """Generate dictionary with a default value of 0"""
    WORDS_TO_COUNT[words] = WORDS_TO_COUNT.get(words, 0) + 1

text = sorted(text)  # Sort in alphabetical order
max_length = max((len(element) for element in text))  # get maximum length of word

for i in WORDS_TO_COUNT:
    """Print word and count with appropriate blank"""
    print(f"{i:{max_length}} : {WORDS_TO_COUNT[i]}")


