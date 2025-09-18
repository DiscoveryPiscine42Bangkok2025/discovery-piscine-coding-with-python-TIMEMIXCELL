#!/usr/bin/env python3
import sys
def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print("none")
        return
    s = args[0]
    result = ""
    for ch in s:
        if ch == 'z':
            result += "z"
    if result:
        print(result)
    else:
        print("none")
main()