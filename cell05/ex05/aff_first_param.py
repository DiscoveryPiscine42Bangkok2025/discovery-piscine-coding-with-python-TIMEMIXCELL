#!/usr/bin/env python3
import sys
def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("none")
    else:
        print(args[0])
main()
