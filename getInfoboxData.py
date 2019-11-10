#!/usr/bin/env python3

import requests as r
import bs4 as bs

url = 'https://en.wikipedia.org/wiki/Terry_Pratchett'

req = r.get(url)

print(req.text)