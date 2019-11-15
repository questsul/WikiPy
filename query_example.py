#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

with open("wiki_data.json", "r", encoding="utf-8") as wiki_json:
    wiki_data = json.load(wiki_json)


print("\nPeople born in England:")
for person in wiki_data:
    try:
        if "England" in person.get("birth_place"):
            print(person.get("person"))
    except TypeError:
        continue


print("\nPerson and their occupation if given.")
for person in wiki_data:
    print(
        "{person} : {occupation}".format(
            person=person.get("person"), occupation=person.get("occupation")
        )
    )


print("\nMusicians:")
for person in wiki_data:
    try:
        if any(
            x in person.get("occupation")
            for x in ["singer", "songwriter", "musician", "composer"]
        ):
            print(person.get("person"))
    except TypeError:
        continue
