#!/usr/bin/env python3
def main():
    def famous_births(women):
        # sort dictionary ตามปีเกิด
        sort = sorted(women.values(), key=lambda x: x["date_of_birth"])
        
        for i in sort:
            print(f"{i['name']} is a great scientist born in {i['date_of_birth']}.")
    women = {
        "ada": {"name": "Ada Lovelace", "date_of_birth": 1815},
        "cecilia": {"name": "Cecilia Payne", "date_of_birth": 1900},
        "lise": {"name": "Lise Meitner", "date_of_birth": 1878},
        "grace": {"name": "Grace Hopper", "date_of_birth": 1906},
    }
    famous_births(women)
main()
