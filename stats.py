def word_count(text):
    words = text.split()
    return = len(words)
    
def letter_count(text):
    counts = {}
    for letter in text.lower():
        counts[letter] = counts.get(letter,0) + 1
    return counts

def sort_on(item):
    return item["num"]

def sort_letters(counts_dict):
    counts = []
    for char, num in counts_dict.items():
        if char.isalpha():
            counts.append({"char": char, "num": num})

    counts.sort(reverse=True, key=sort_on)
    return(counts)
