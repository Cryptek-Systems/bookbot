
from stats import word_count, letter_count

def get_book_text(path):

    with open(path) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)
    print(word_count(text))
    print(letter_count(text))

main()

