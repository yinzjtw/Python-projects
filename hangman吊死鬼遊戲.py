"""
This program plays hangman game.
Users see a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random


# This constant controls the number of guess the player has.
N_TURNS = 7


def main():
    word = random_word()
    word_covered = ''
    for ch in word:
        word_covered += '-'

    lives = N_TURNS

    print('The word looks like ' + word_covered)
    print('You have ' + str(lives) + ' wrong guesses left.')
    while True:
        if lives == 0:
            print('You are completely hung :(')
            break
        else:
            guess = input('Your guess: ')
            if guess.isalpha() and len(guess) == 1:
                guess = guess.upper()
                if word.find(guess) != -1:
                    print('You are correct!')
                    for i in range(len(word)):
                        if word[i] == guess:
                            word_covered = word_covered[:i] + guess + word_covered[i+1:]
                    if word_covered.isalpha():  # all figure out
                        print('You win!!')
                        break
                    else:
                        print('The word looks like ' + word_covered)
                        print('You have ' + str(lives) + ' wrong guesses left.')
                else:
                    lives -= 1
                    print('There\'s no ' + guess + '\'s in the word.')
                    print('The word looks like ' + word_covered)
                    print('You have ' + str(lives) + ' wrong guesses left.')
            else:
                print('Illegal format.')
    print('The word was: ' + word)


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
