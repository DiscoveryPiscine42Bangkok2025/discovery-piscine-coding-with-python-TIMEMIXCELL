#!/usr/bin/env python3
import sys
def shrink(s):
    return s[:8]
def enlarge(s):
    return s + "Z" * (8 - len(s))
def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print("none")
    else:
        for i in args:
            if len(i) > 8:
                print(shrink(i))
            elif len(i) < 8:
                print(enlarge(i))
            else:
                print(i)
main()
