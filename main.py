from stats import get_num_words

def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        file_contents = f.read()

        return file_contents

def main():
    print(f"Found {get_num_words(get_book_text('books/frankenstein.txt'))} total words")

main()