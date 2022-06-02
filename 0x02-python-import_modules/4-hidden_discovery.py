#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    hiddenList = dir(hidden_4)
    for i in range(len(hiddenList) -1):
        if ("__" not in hiddenList[i]):
            print(hiddenList[i])
