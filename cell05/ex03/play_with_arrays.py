#!/usr/bin/env python3
def main():
    original = [2, 8, 9, 48, 8, 22, -12, 2]
    new_array = []
    for num in original:
        if num > 5:
            new_array.append(num + 2)
    unique = set(new_array)
    print("Original array:", original)
    print("New array:", unique)
main()
