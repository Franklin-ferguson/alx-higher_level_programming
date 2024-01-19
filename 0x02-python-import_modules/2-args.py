#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    aglist = len(sys.argv) - 1
    if aglist == 0:
        print("0 arguments")
    elif aglist == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(aglist))
    for i in range(aglist):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
