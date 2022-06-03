#!/usr/bin/python3
def multiple_returns(sentence):
    len_sen = len(sentence)
    if (sentence == ""):
        first = None
    else:
        first = sentence[0]
        return (len_sen, first)
