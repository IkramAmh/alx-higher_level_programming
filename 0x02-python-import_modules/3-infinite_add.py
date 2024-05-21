#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    c = len(sys.argv)
    sm = 0
    if c == 1:
        print("0")
    else:
        for i in range(1, c):
            sm = sm + int(sys.argv[i])
        print("{}".format(sm))
