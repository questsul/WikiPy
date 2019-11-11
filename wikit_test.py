import wptools as wp
import re
import bs4

clean_patt = re.compile(r'[\[\]\{\}]')

page = wp.page('Terry_Pratchett')

parse = page.get_parse()

# for key, value in parse.data['infobox'].items():
#     print(key, ' : ', re.sub(clean_patt, '', value).replace('|', ' '))

for key, value in parse.data['infobox'].items():
         print(key, ' : ', ''.join(list(bs4.BeautifulSoup(value, 'lxml').stripped_strings)))