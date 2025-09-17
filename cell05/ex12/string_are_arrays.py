#!/usr/bin/env python3
import sys
def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print("none")
        return
    s = args[0]
    found = False
    for i in s:
        if i == 'z':
            print("z")
            found = True
    if not found:
        print("none")
main()