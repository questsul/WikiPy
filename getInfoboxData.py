#!/usr/bin/env python3

import requests as r
import bs4


title = 'Arsène_Wenger' #Terry_Pratchett Arsène_Wenger Bill_Clinton
url = "http://en.wikipedia.org/wiki/{title}".format(title=title)

req = r.get(url)



soup = bs4.BeautifulSoup(req.text, 'lxml')

infobox_table = soup.find('table', {'class': 'infobox vcard'}).findAll('tr')

infobox = {}
for row in infobox_table:
    if row.text:
        print(row.name, " : ", row.text)
        for child in row.children:
            for sibling in child.next_siblings:
                try:
                    print(child.string, " ; ", sibling.text)
                except AttributeError:
                    continue
    else:
        continue