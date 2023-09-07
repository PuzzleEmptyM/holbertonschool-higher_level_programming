#!/usr/bin/python3

def uppercase(s):
    for char in s:
        diff = ord('a') - ord('A') if 'a' <= char <= 'z' else 0
        print("{}".format(chr(ord(char) - diff)), end='')
    print()


if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
