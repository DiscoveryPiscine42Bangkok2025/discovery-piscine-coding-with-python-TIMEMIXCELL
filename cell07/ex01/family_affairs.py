#!/usr/bin/env python3
def main():
    def find_the_redheads(family):
        red = filter(lambda name: family[name] == "red", family.keys())
        return list(red)
    family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
        }
    print(find_the_redheads(family))
main()
