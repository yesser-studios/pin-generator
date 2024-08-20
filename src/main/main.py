import random
import sys


def gen_random_digit() -> int:
    digit = random.randint(0, 10)
    return digit


def gen_num(digits: int) -> int:
    number: int = 0
    for i in range(0, digits):
        digit = gen_random_digit()
        number *= 10
        number += digit
    return number


def format_number(number: int, digits: int) -> str:
    string = str(number)
    return string.rjust(digits, "0")


def main(digits: int):
    number = gen_num(digits)
    print(format_number(number, digits))


if __name__ == "__main__":
    for i in range(int(sys.argv[2])):
        main(int(sys.argv[1]))

