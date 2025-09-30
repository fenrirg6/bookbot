from stats import get_num_words, get_count_characters, sort_count_characters

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        file_contents = f.read()

        return file_contents

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at", "books/frankenstein.txt", "...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(get_book_text('books/frankenstein.txt'))} total words")
    print("--------- Character Count -------")

    for key in sort_count_characters(get_count_characters(get_book_text('books/frankenstein.txt'))):
        print(f"{key}: {get_count_characters(get_book_text('books/frankenstein.txt'))[key]}")


main()