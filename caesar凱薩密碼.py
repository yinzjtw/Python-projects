"""
This program demonstrates the idea of caesar cipher.
Users will be asked to input a number to produce shifted
ALPHABET as the cipher table. After that, any strings typed
in will be encrypted.
"""


# This constant shows the original order of alphabetic sequence.
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    secret_number = int(input('Secret number: '))
    new_alphabet = ALPHABET[len(ALPHABET)-secret_number:] + ALPHABET[:len(ALPHABET)-secret_number]

    message = input('What\'s the ciphered string? ')
    message = message.upper()
    ans = ''
    for ele in message:
        if ele.isalpha():
            ans += ALPHABET[new_alphabet.find(ele)]
        else:
            ans += ele
    print('The deciphered string is: '+ans)


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
