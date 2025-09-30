import sys
from stats import get_num_words, get_count_characters, sort_count_characters

if len (sys.argv) < 2:
    print('Usage: python3 main.py <path_to_book>')
    sys.exit(1)

filepath = sys.argv[1] # second argument as a path to the book file

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        file_contents = f.read()

        return file_contents

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at", filepath, "...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text(filepath))} total words")
    print("--------- Character Count -------")

    for key in sort_count_characters(get_count_characters(get_book_text(filepath))):
        print(f"{key}: {get_count_characters(get_book_text(filepath))[key]}")


main()