def find_substrings(main_string, sub_string):
    """
    Function to find all occurrences of a substring in a string.

    Args:
    - main_string: The main string to search within.
    - sub_string: The substring to search for.

    Returns:
    - A list of indices where the substring is found.
    """
    substring_indices = []
    len_main = len(main_string)
    len_sub = len(sub_string)

    for i in range(len_main - len_sub + 1):
        if main_string[i:i + len_sub] == sub_string:
            substring_indices.append(i)

    return substring_indices

def main():
    # Read the words from words.txt
    with open("words.txt", "r") as words_file:
        words = words_file.read().splitlines()

    # Read the filter words from filter.txt
    with open("filter.txt", "r") as filter_file:
        filter_words = filter_file.read().splitlines()

    filtered_words = []

    # Iterate through each word in words.txt
    for word in words:
        # Flag to check if any filter word is found in the current word
        found = False
        # Iterate through each filter word
        for filter_word in filter_words:
            # Check if filter word is a substring of the current word
            indices = find_substrings(word, filter_word)
            if indices:
                found = True
                filtered_words.append((word, filter_word, indices))
                break  # Stop checking further filter words if found in this word

        # If no filter word was found in the current word, write it to output
        if not found:
            with open("output.txt", "a") as output_file:
                output_file.write(word + "\n")

    # Output filtered words to terminal
    for word, filter_word, indices in filtered_words:
        print(f"Word '{word}' contains '{filter_word}' at index/indices:", indices)

if __name__ == "__main__":
    main()
