#!/usr/bin/env python3
import sys
def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("none")
        return
    for i in args:
        if i.endswith("ism"):
            continue
        print(i + "ism")
main()
