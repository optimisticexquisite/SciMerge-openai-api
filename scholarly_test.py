import json
from scholarly import scholarly
search_query = scholarly.search_pubs('Title:Gravitational Waves, a new way of explaining the universe')
for i in search_query:
    print(i)