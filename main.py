from os import urandom

while True:
    try:
        length = int(input("Length for password: "))
        if length <= 0:
            raise ValueError
        break
    except ValueError:
        print("Invalid length")
    except (EOFError, KeyboardInterrupt):
        exit()

passleng = 0

while True:
    if passleng == length:
        break
    try:
        char = urandom(1).decode("UTF-7")
        if ord(char) > 32 and ord(char) < 127:
            passleng += 1
            print(char, end="")
    except (UnicodeDecodeError, TypeError):
        pass

print()
