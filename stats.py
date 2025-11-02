def count_words(text):
    """Count and return the number of words in the text."""
    words = text.split()
    return len(words)


def count_characters(text):
    """Count and return the number of times each character appears in the text.

    Characters are converted to lowercase to avoid duplicates.
    Returns a dictionary with character -> count mappings.
    """
    char_counts = {}
    lowered_text = text.lower()

    for char in lowered_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts


def sort_character_counts(char_counts):
    """Sort character counts and return a list of dictionaries.

    Takes a dictionary of character counts and returns a sorted list
    of dictionaries with 'char' and 'num' keys, sorted by count descending.
    """

    def sort_on(dict_item):
        """Helper function to get the 'num' key for sorting."""
        return dict_item["num"]

    # Convert dictionary to list of dictionaries
    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})

    # Sort by count from greatest to least
    char_list.sort(reverse=True, key=sort_on)

    return char_list
