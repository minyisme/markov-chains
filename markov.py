from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file_text = open(file_path).read()

    file_text = file_text.replace("\n"," ").rstrip()

    return file_text


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}

    # your code goes here
    text_list = text_string.split()
    # Iterates through the list of words to create tuples (bi-grams)
    # Those tuples become dictionary keys with a default value of []
    for x in range(len(text_list)-1):
        text_key = (text_list[x], text_list[x + 1])
        # If statement handles 1st entry of key-value and subsequent
        if text_key not in chains:
            try:
                chains[text_key] = [text_list[x+2]]
            except IndexError:
                chains[text_key] = [None]
        else:
            try:
                chains[text_key].append(text_list[x+2])
            except IndexError:
                chains[text_key].append(None)

    return chains


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    text = ""

    #Initializing words_list with random tuple
    words_list = list(choice(chains.keys())) 

    #Appends new word to words_list based using last 2 words of words_list as key
    while words_list[-1] != None:
        tuple_to_look_up = (words_list[-2], words_list[-1])
        a_list_of_words = chains[tuple_to_look_up]
        new_word = choice(a_list_of_words)
        words_list.append(new_word)

    #Joins words_list as string called text
    text = " ".join(words_list[:-1])

    return text


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text

