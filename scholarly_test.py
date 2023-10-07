import json
from scholarly import scholarly
search_query = scholarly.search_pubs("Title:'Working with virtual assistance for blind people\n\nAbstract: The aim of this project is to develop a virtual assistance for blind people so that they can use the software communicate seamlessly with their other different senses.")
for i in search_query:
    print(i)