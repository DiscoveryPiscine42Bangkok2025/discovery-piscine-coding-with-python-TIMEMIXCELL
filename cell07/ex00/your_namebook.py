#!/usr/bin/env python3
def main():
    def array_of_names(person):
        result = []
        for first, last in person.items():
            fullname = first.capitalize() + " " + last.capitalize()
            result.append(fullname)
        return result
    persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
    print(array_of_names(persons))
main()