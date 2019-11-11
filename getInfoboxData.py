#!/usr/bin/env python3

import requests as r
import bs4


title = 'Terry_Pratchett' #Terry_Pratchett Arsène_Wenger Bill_Clinton
url = "http://en.wikipedia.org/wiki/{title}".format(title=title)

req = r.get(url)



soup = bs4.BeautifulSoup(req.text, 'lxml')


infobox = soup.find('table', {'class': 'infobox vcard'})

infobox_table = infobox.tbody

info = []
for child in infobox_table:
    info.append(child.text.split('\n'))
print(info)