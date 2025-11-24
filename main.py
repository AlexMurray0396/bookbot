# To do: add new books

from stats import get_book_text, get_word_count, get_character_counts, dict_list
import sys

if len(sys.argv) == 1:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:

    print("============ BOOKBOT ============")

    file = sys.argv[1]

    print(f"Analyzing book found at {file}...")

    book = get_book_text(file)

    print("----------- Word Count ----------")

    word_count = get_word_count(book)

    print(f"Found {word_count} total words")

    print("--------- Character Count -------")

    char_counts = get_character_counts(book)

    char_dict = dict_list(char_counts)

    for item in char_dict: 
        if item['char'].isalpha():
            print(f"{item['char']}: {item['num']}")
        else:
            continue