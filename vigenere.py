import sys


def vigenere():
    """
    Uses alphphabetic key word provided on command line to encrypt plaintext entered
    at the prompt.  Prints the reulting encoded message using Vigenere's algorithm.
    """
    if len(sys.argv) != 2:
        sys.exit("Must specify alphabetic key to use for encrpyting message")
    key_len = len(sys.argv[1])
    for i in range(key_len):
        if not sys.argv[1][i].isalpha():
            sys.exit("Only alhpabetic characters allowed in key")
    plaintext = input("plaintext: ")
    length = len(plaintext)
    k = 0
    print("ciphertext: ", end="")
    for letter in plaintext:
        if not letter.isalpha():
            print(letter, end="")
        else:
            if key_len == k:  # check to see if we've run out of characters
                k = 0  # start over at beginning of key
            if letter.isupper():
                c = chr((ord(letter) + ord(sys.argv[1][k].upper()) -
                         2 * ord('A')) % 26 + ord('A'))
                print(c, end="")
                k += 1
            else:
                c = chr((ord(letter) - ord('a') + ord(sys.argv[1][k].upper()) -
                        ord('A')) % 26 + ord('a'))
                print(c, end="")
                k += 1
    print()

if __name__ == "__main__":
    vigenere()
