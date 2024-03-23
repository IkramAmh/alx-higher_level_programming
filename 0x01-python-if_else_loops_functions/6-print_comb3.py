#!/usr/bin/python3
for i in range(48, 56):
    for j in range(48, 58):
        if i == j:
            continue
        elif i < j:
            print("{}".format(chr(i) + chr(j)), end=", ")
print("{}".format(chr(56) + chr(57)), end="\n")
