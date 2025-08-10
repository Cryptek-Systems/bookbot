
import sys
from stats import word_count, letter_count, sort_letters

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path = sys.argv[1]

def get_book_text(path):

    with open(path) as f:
        return f.read()

def main():
    text = get_book_text(book_path)

    num_words = word_count(text)                # get integer count here
    counts_dict = letter_count(text)
    sorted_counts = sort_letters(counts_dict)

    print_report(book_path, num_words, sorted_counts)  # pass int, not function

def print_report(book_path, word_count, sorted_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count -----------")
    print(f"Found {word_count} total words")  # word_count is now an int
    print("--------- Character Count -------")
    for item in sorted_counts:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

        


main()

