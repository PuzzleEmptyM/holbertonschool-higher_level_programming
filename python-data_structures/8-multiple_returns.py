#!/usr/bin/python3

def multiple_returns(sentence):
    """Return a tuple with the length and first character of a string."""
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
