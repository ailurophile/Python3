import sys


def credit():
    """
    Program which takes a credit card number on the command line & returns
    the type of card as a string: AMEX, VISA, MASTERCARD, INVALID.
    """
    typed = input("Number: ")  # get credit card number
    if not typed.isdigit():
        sys.exit("Only digits may be entered.")
    num = int(typed)
    sum = 0
    digits = 0
    type = "INVALID"
    while (num >= 1000):
        digit1 = num % 10
        sum += digit1
        num //= 10
        digit2 = (num % 10) * 2
        if digit2 > 9:
            digit2 = 1 + digit2 % 10
        sum += digit2
        num //= 10
        digits += 2  # keep count of digits to check for 13
    test = num
    if test > 99:  # get top two digits
        test //= 10
    if test in {34, 37}:
        type = "AMEX"
    elif test in range(51, 56):
        type = "MASTERCARD"
    elif test in range(40, 50):
        type = "VISA"
    # continue processing in pairs
    while (num >= 9):
        digit1 = num % 10
        sum += digit1
        num //= 10
        digit2 = (num % 10) * 2
        if digit2 > 9:
            digit2 = 1 + digit2 % 10
        sum += digit2
        num //= 10
        digits += 2
    if digits == 12 and num == 4:
        type == "VISA"
    sum += num  # process last digit if any
    if sum % 10 != 0:
        type = "INVALID"
    print(type)


if __name__ == "__main__":
    credit()
