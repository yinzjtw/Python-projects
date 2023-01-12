"""
File: boggle.py
Name: Jay Yin
----------------------------------------
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
	"""
	Ask user to input 16 letters, and check if are all in legal format.
	Use dictionary ''lst_letter'' to store all the letters, and record the letter's position.
	→ key: (col ,row), value: letter

	Use boggle function to find words started with certain letter, and composed by sequences of adjacent letters.
	"""
	start = time.time()
	####################
	dict_letter = {}
	for i in range(4):
		row = input(f'{i+1} row of letters: ')
		if row_checker(row):   # check if inputted letters are in legal format
			row = row.lower()
			for j in range(4):
				dict_letter[(j+1, i+1)] = row[j*2]
		else:
			print('Illegal input')
			break
	boggle(dict_letter)

	####################
	end = time.time()
	print('----------------------------------')
	print(f'The speed of your boggle algorithm: {end - start} seconds.')


def row_checker(row):
	"""
	:param row: (str) the string user inputted.
	:return:　(bool) Whether the inputted row is legal or not.
	"""
	if len(row) != 7:
		return False
	else:
		for i in range(4):
			if not row[i*2].isalpha():
				return False
		for i in range(3):
			if not row[1+i*2] == ' ':
				return False
	return True


def boggle(dict_letter):
	"""
	Loop over each letter,
	look for words started with given letter, and composed by sequences of adjacent letters.

	:param dict_letter: (dictionary) letters user inputted. key: (col ,row), value: letter
	"""
	words = []
	for i in range(1, 5):
		for j in range(1, 5):
			ch = dict_letter[(i, j)]
			dictionary = read_dictionary(ch)
			boggle_helper(dict_letter, dictionary, words, '', i, j, [])
	print(f'There are {len(words)} words in total.')  # words (list) stored in heap→　passed by reference


def boggle_helper(dict_letter, dictionary, words, word, x, y, letter_used):
	"""
	:param dict_letter: (dictionary) letters user inputted. key: (col ,row), value: letter
	:param dictionary: (list) list contains selected words from the FILE 'dictionary'.
	:param words: (list) list stores all the founded words.
	:param word: (str) the word to be checked if it's legal to be added in 'words'.
	:param x: (int) column order of the letter
	:param y: (int) row order of the letter
	:param letter_used: (list) stored the position (col, row) of used letters

	To find words in dictionary that started with certain letter and length >= 4.
	"""
	# using for loop→　function will stop without setting base case
	for i in range(-1, 2):
		for j in range(-1, 2):
			# Choose
			new_x = x + i
			new_y = y + j
			if 1 <= new_x <= 4 and 1 <= new_y <= 4 and (new_x, new_y) not in letter_used:
				word += dict_letter[(new_x, new_y)]
				letter_used.append((new_x, new_y))

				if len(word) >= 4 and word in dictionary and word not in words:
					words.append(word)
					print(f'Found "{word}"')

				# Explore
				if has_prefix(dictionary, word):
					# use new_x, new_y, so the x, y won't change when get back to previous layer of recursion.
					boggle_helper(dict_letter, dictionary, words, word, new_x, new_y, letter_used)

				# Un-choose
				word = word[:len(word) - 1]
				letter_used.pop()


def read_dictionary(ch):
	"""
	:param ch : (str)

	This function reads file "dictionary.txt" stored in FILE
	and appends selected words in each line into a Python list
	Selecting criteria: 1) word starts with "ch" 2) length >= 4
	"""
	lst_dictionary = []
	with open(FILE, 'r') as dictionary:
		for word in dictionary:
			word = word.strip()
			if word.startswith(ch) and len(word) >= 4:
				lst_dictionary.append(word)
	return lst_dictionary


def has_prefix(dictionary, sub_s):
	"""
	:param dictionary: (list) A list contains selected words from the FILE 'dictionary'.
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
