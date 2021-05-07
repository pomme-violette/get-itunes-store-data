import requests
import pprint


url = "https://itunes.apple.com/search"
payload = {"term": "",
           "country": "", # ISO 3166-1 alpha-2
           "media": "", 
           "entity": "",
           "attribute": "",
           "callback": "",
           "limit": "",
           "lang": "",
           "version": "",
           "explicit": "",
           }


r = requests.get(url, params=payload)

pprint.pprint(r.text)
