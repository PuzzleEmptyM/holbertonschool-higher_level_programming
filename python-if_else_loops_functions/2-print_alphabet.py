#!/usr/bin/python3

for char in range(ord('a'), ord('z') + 1):
    print("{:c}".format(char), end='')

# Print a newline character to separate the output from the shell prompt
print()
