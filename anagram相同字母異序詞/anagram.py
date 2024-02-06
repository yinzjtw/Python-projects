"""
This program recursively finds all the anagram(s)
for the word (if it's in the flile "dictionary") input by user,
and terminates when the input string matches the EXIT constant (-1).

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    Ask user to input word and find the corresponding anagrams.
    Stop when user enter "EXIT".
    """
    start = time.time()
    ####################
    print("Welcome to stanCode \"Anagram Generator\" (or -1 to quit)")
    while True:
        word = str(input('Find anagrams for: '))
        if word == EXIT:
            break
        else:
            print('Searching...')
            find_anagrams(word)
    ####################
    end = time.time()
    print('----------------------------------')
    print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    lst_dictionary = []
    with open(FILE, 'r') as dictionary:
        for word in dictionary:
            word = word.strip()
            lst_dictionary.append(word)
    return lst_dictionary


def find_anagrams(s):
    """
    :param s: str, word to find the corresponding anagrams.
    """
    lst_dictionary = read_dictionary()
    anagrams = []
    find_anagrams_helper(s, '', anagrams, lst_dictionary, len(s))
    print(f'{len(anagrams)} anagrams: {anagrams}')


def find_anagrams_helper(s, anagram, anagrams, lst_dictionary, len_s):
    """
    :param s: str, word to find the corresponding anagrams.
    :param anagram: str. Empty at first, contain potential anagram after each recursion.
    :param anagrams: list. Empty at first, and will contain all the anagrams at last.
    :param lst_dictionary: list, contains all the words in dictionary.
    :param len_s: int, the length of s.
    """
    if len(anagram) == len_s and anagram in lst_dictionary:
        if anagram not in anagrams:
            anagrams.append(anagram)
            print(f'Found:{anagram}')
            print('Searching...')
    else:
        for i in range(len(s)):
            anagram += s[i]
            new_s = s[:i]+s[i+1:]
            if has_prefix(lst_dictionary, anagram):
                find_anagrams_helper(new_s, anagram, anagrams, lst_dictionary, len_s)
            anagram = anagram[:len(anagram)-1]


def has_prefix(lst_dictionary, sub_s):
    """
    Loop over lst_dictionary to find out if there's any word (element of the list) start with sub_s.
    :param lst_dictionary: list
    :param sub_s: str
    :return: True→　there's word in lst_dictionary start with sub_s.
             False→　there's no word in lst_dictionary start with sub_s.
    """
    for word in lst_dictionary:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
