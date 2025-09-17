#!/usr/bin/env python3
import sys
def main():
    args = sys.argv[1:]

    if len(args) < 2:
        print("none")
    else:
        for i in reversed(args):
            print(i)
main()
