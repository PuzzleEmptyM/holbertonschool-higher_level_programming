#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    total = 0
    for arg in args:
        total += int(arg)
    print(total)
