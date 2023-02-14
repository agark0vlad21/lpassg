from os import urandom
from argparse import ArgumentParser

Parser = ArgumentParser(description="Simple password generator")
Parser.add_argument("-l", "--length", help="Length of password", type=int, default=8)
args, unknown = Parser.parse_known_args()  # Unrecognised args will be ignored

passleng = 0  # Length counter for password

while True:
    if passleng == args.length:
        break
    try:
        char = urandom(1).decode("UTF-7")
        if ord(char) > 32 and ord(char) < 127:
            passleng += 1
            print(char, end="")
    except (UnicodeDecodeError, TypeError):
        pass

print()
