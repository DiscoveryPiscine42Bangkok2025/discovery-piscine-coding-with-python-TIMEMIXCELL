#!/usr/bin/env python3
import sys
def downcase_it(text):
    return text.lower()
def main():
    args = sys.argv[1:]

    if len(args) == 0:
        print("none")
    else:
        for i in args:
            print(downcase_it(i))
main()
