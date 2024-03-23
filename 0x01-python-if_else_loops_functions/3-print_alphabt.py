#!/usr/bin/python3
for i in [x for x in range(97, 123) if (x != 101) & (x != 113)]:
    print("{}".format(chr(i)), end="")
