def word_count(text):
    words = text.split()
    num_words = len(words)
    words = f"{num_words} words found in the document"
    return(words)

def letter_count(text):
    counts = {}
    for letter in text.lower():
        counts[letter] = counts.get(letter,0) + 1
    return counts