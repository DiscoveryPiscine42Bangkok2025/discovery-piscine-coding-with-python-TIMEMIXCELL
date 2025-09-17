#!/usr/bin/env python3
import sys
def main():
    args = sys.argv[1:]

    if len(args) != 1:
        print("none")
    else:
        print(args[0].lower())
main()