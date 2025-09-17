#!/usr/bin/env python3
import sys
import re

def main():
    args = sys.argv[1:]
    if len(args) != 2:
        print("none")
        return

    keyword = args[0]
    text = args[1]
    matches = re.findall(rf"{re.escape(keyword)}", text) #คืนลิสต์ของ match ทั้งหมด

    if matches:
        print(len(matches))
    else:
        print("none")
main()
