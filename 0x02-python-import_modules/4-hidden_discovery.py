#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    import sys
    hiddenList = dir(hidden_4)
    hiddenList.sort()
    
    for i in range(len(hiddenList) - 1):
        if (hiddenList[i][0] != '_'):
            print(hiddenList[i])
