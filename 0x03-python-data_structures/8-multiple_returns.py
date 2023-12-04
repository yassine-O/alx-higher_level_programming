#!/usr/bin/python3

def multiple_returns(sentence):
    n = len(sentence)
    return (n, sentence[0] if n > 0 else None)
