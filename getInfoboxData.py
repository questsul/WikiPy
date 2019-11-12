#!/usr/bin/env python3

import requests as r
import bs4


title = 'Terry_Pratchett' #Terry_Pratchett Arsène_Wenger Bill_Clinton
url = "https://en.wikipedia.org/wiki/{title}".format(title=title)

req = r.get(url)



soup = bs4.BeautifulSoup(req.text, 'lxml')


infobox = soup.find('table', {'class': 'infobox vcard'})

infobox_table = infobox.tbody

info = []
for child in infobox_table:
    info.append(child.text.split('\n'))
print(info)


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
"Peyton_Manning"
"Diana_Princess_of_Wales",
"Bill_Cosby",
"Jerry_Seinfeld",
"Elvis_Presley",
"Heidi_Klum",
"Aristotle",