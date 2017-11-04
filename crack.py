import sys
import crypt
import string


def crack():
"""
Program to decrypt passwords of 1-4 letters (only alphpa) encrypted
with DES encryption & a salt value of "50".
"""
    def test(password):
        if crypt.crypt(password, salt) == hash:
            print(password)
            return True  # found password
        return False

    if len(sys.argv) != 2:
        print("Usage: python crack.py hash")
        return 1
    hash = sys.argv[1]
    salt = "50"
    # try single letter passwords
    for a in string.ascii_letters:
        if test(a):
            return 0
        for b in string.ascii_letters:
            if test(a + b):
                return 0
            for c in string.ascii_letters:
                if test(a + b + c):
                    return 0
                for d in string.ascii_letters:
                    if test(a + b + c + d):
                        return 0
    return 1  # password not found

if __name__ == "__main__":
    crack()
