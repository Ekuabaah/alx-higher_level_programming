#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    summation = 0
    for arg in argv[1:]:
        summation += int(arg)
    print(summation)
