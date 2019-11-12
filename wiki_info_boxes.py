#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Script for retriwing data from wikipedia infoboxes.
## Usage: 
##      python wiki_info_boxes.py
## Data will be stored in a working directory to json file: wiki_data.json

import wptools as wp
import re
import json

# Random list of famous people prefomatted to work with wikipedia url.
PEOPLE = [
    "Walt_Disney",
    "Nostradamus",
    "Tina_Fey",
    "Taylor_Swift",
    "Mel_Blanc",
    "Stephen_King",
    "Steve_Carell",
    "Toby_Keith",
    "Jeff_Gordon",
    "William_Wallace",
    "Harriet_Tubman",
    "Brad_Pitt",
    "Robin_Hood",
    "Dwight_Howard",
    "Amelia_Earhart",
    "Harry_S_Truman",
    "Britney_Spears",
    "Paul_McCartney",
    "Maria_Sharapova",
    "Galileo_Galilei",
    "Eva_Longoria",
    "David_Copperfield",
    "Chuck_Lorre",
    "Peyton_Manning",
    "Diana_Princess_of_Wales",
    "Bill_Cosby",
    "Jerry_Seinfeld",
    "Elvis_Presley",
    "Heidi_Klum",
    "Aristotle",
]


def get_infobox(person):
    """
    Retrieves data from Wikipedia using wptools and Parse API for given person.
    """
    try:
        page = wp.page(person, show=False, silent=True, verbose=False)
        parse = page.get_parse(show=False, timeout=15)
        return parse.data.get("infobox")
    except LookupError:
        print("{person} not found!!".format(person=person))
        return None


def clean_values(value):
    """
    Performs small data cleansing
    """
    value = re.sub(r"[\[\]\{\}]", "", value)
    value = re.sub(r"[\|]", " ", value)
    value = re.sub(r"<[^<]+?>", " ", value)
    value = re.sub(r"(?i)\{\{cite .*\}\}", "", value)
    value = re.sub(r"&nbsp;", "", value)
    return value


def prep_data(infobox, person):
    """
    Formats the output dictionary
    """
    personal_info = {}
    for key, value in infobox.items():
        # ignoring useless fields
        if key not in [
            "image",
            "signature",
            "signature_alt",
            "module",
            "caption",
            "colour",
            "image_size",
            "image_upright",
            "alt",
            "module2",
        ]:
            personal_info[key] = clean_values(value)
    personal_info["person"] = person
    personal_info["url"] = "https://en.wikipedia.org/wiki/{title}".format(title=person)
    return personal_info


def main():
    output = []
    for person in PEOPLE:
        infobox = get_infobox(person)
        if infobox:
            data = prep_data(infobox, person)
            output.append(data)
        else:
            print("No infobox for {person}".format(person=person))
            continue
    with open("wiki_data.json", "w", encoding="utf-8") as json_file:
        json_file.write(json.dumps(output, indent=4, ensure_ascii=False))


if __name__ == "__main__":
    main()
