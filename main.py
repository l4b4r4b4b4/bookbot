import sys

from stats import count_words, count_characters, sort_character_counts


def get_book_text(filepath):
    """Read and return the contents of a file as a string."""
    with open(filepath) as f:
        return f.read()


def main():
    """Main function to read and analyze a book from command line argument."""
    # Check if book path argument was provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    # Print header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")

    # Print word count
    print("----------- Word Count ----------")
    num_words = count_words(text)
    print(f"Found {num_words} total words")

    # Print character count
    print("--------- Character Count -------")
    char_counts = count_characters(text)
    sorted_chars = sort_character_counts(char_counts)

    for char_dict in sorted_chars:
        char = char_dict["char"]
        num = char_dict["num"]
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {num}")

    # Print footer
    print("============= END ===============")


if __name__ == "__main__":
    main()
