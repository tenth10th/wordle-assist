def load_five_letter_words():
    possible_words = list()
    with open('five-letter-english-words.txt') as file_handle:
        for line in file_handle:
            # Skip any Python-style comment lines
            if line.startswith("#"):
                continue
            # Each line should be a word + linebreak - remove whitespace
            word = line.strip()
            possible_words.append(word)
    return possible_words


def wordle_assist(possible_words):
    starting_word_count = len(possible_words)
    print(f"Starting with {starting_word_count:,} possible 5-letter words:")

    print(", ".join(possible_words))

    ending_word_count = len(possible_words)
    decrease = starting_word_count - ending_word_count
    decrease_percent = round((decrease / starting_word_count) * 100, 2) if decrease else decrease
    print(f"Ending with {ending_word_count:,} remaining 5-letter words, a decrease of {decrease_percent}%")


if __name__ == "__main__":
    possible_words = load_five_letter_words()
    wordle_assist(possible_words)
