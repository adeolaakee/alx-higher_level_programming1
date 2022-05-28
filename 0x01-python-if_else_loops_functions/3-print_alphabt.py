#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    if c == 101 and c == 113:
        continue
    print("{:c}".format(c), end="")
