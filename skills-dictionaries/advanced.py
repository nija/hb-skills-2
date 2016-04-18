#!/usr/bin/env python
# The above line is an environment directive; please ignore it
"""Advanced skills-dictionaries.

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    char_frequency = { }

    # This should be able to be done with a dictionary comprehension, but my brain is too tired 
    # right now, so I'm doing it this way

    # Split phrase into chars
    for word in phrase.split():
        for char in word:
            # Use the number of times char appears in the phrase as the key
            frequency = phrase.count(char)
            if frequency in char_frequency:
                # The value is the list of chars
                char_frequency[frequency].append(char)
                # De-dup the list
                char_frequency[frequency] = list(set(char_frequency[frequency]))
            else:
                # Set the value as a list with the initial list element being char
                char_frequency[frequency] = [char]

    # Get the highest count
    desired_key = sorted(char_frequency.keys()).pop()
    return char_frequency[desired_key]



def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """

    word_lengths = {}

    for word in words:
        if len(word) in word_lengths:
            word_lengths[len(word)].append(word)
            # Just added this line to the similar answer in skills-dictionaries
            word_lengths[len(word)].sort()
        else:
            word_lengths[len(word)] = [word]

    return sorted(word_lengths.items())


#####################################################################
# You can ignore everything below this.


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
