#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        print("{}".format(chr(ord(str[i]) - 32)) if ((ord(str[i])) >= 97) & \
((ord(str[i])) <= 122) else "{}".format(str[i]), end="")
    print("\n")
