#!/usr/bin/python3

def islower(c):
    # Check if ASCII value of character falls within lowercase ASCII range
    return ord('a') <= ord(c) <= ord('z')


if __name__ == "__main__":
    islower = __import__('7-islower').islower

    print("a is {}".format("lower" if islower("a") else "upper"))
    print("H is {}".format("lower" if islower("H") else "upper"))
    print("A is {}".format("lower" if islower("A") else "upper"))
    print("3 is {}".format("lower" if islower("3") else "upper"))
    print("g is {}".format("lower" if islower("g") else "upper"))
