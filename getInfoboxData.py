#!/usr/bin/env python3

import requests as r
import bs4


title = 'Terry_Pratchett' #'Arsène_Wenger'
url = "http://en.wikipedia.org/wiki/{title}".format(title=title)

req = r.get(url)



soup = bs4.BeautifulSoup(req.text, 'lxml')

infobox_table = soup.find('table', {'class': 'infobox vcard'}).findAll('tr')

infobox = {}
for row in infobox_table:
    print(row.string)
    for child in row.descendants:
        for sibling in child.next_siblings:
            print(child.string, " ; ", sibling.string)