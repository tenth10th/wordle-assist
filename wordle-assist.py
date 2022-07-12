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

green = {'r': 2}
gray = ['salnchumptid']
yellow = {'o': 3, 'e': 3}

def wordle_assist(possible_words):
    starting_word_count = len(possible_words)
    print(f"Starting with {starting_word_count:,} possible 5-letter words:")

    new_possible_words = list()
    for word in possible_words:
        keep_word = True
        # Green letter hints
        for letter, position in green.items():
            if word[position] != letter:
                keep_word = False

        # Yellow letter hints
        for letter, position in yellow.items():
            if letter not in word:
                keep_word = False
            if word[position] == letter:
                keep_word = False
        
        # Gray letter hints
        for ch in gray[0]:
            if ch in word:
                keep_word = False
                
        if keep_word:
            new_possible_words.append(word)

    print(", ".join(new_possible_words))

    ending_word_count = len(new_possible_words)
    decrease = starting_word_count - ending_word_count
    decrease_percent = round((decrease / starting_word_count) * 100, 2) if decrease else decrease
    print(f"Ending with {ending_word_count:,} remaining 5-letter words, a decrease of {decrease_percent}%")


if __name__ == "__main__":
    possible_words = load_five_letter_words()
    wordle_assist(possible_words)
