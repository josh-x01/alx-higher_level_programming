#!/usr/bin/python3
import sys
import hidden_4
if __name__ == '__main__':
    wordKeys = dir(hidden_4)
    lenwords = len(wordKeys)

    for i in range(lenwords):
        if wordKeys[i][0] != '_':
            print(wordKeys[i])
