# A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once(case is irrelevant).

# Given a string, detect whether or not it is a pangram. Return True if it is , False if not. Ignore numbers and punctuatio


def is_pangram(s):
    alphabet_ = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12,
                 'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24, 'z': 26}
    for letter in s:
        if letter.lower() in alphabet_:
            del alphabet_[letter.lower()]
        else:
            continue
        print(len(alphabet_))
    if len(alphabet_) == 0:
        return True
    if len(alphabet_) != 0:
        return False
