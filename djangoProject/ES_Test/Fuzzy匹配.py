from elasticsearch_dsl import *
from elasticsearch_dsl.query import *

connections.create_connection(hosts=['localhost'])

def search_query(search,query,columns):
    s=search.query(query)
    response=s.execute()

    for hit in response.hits:
        for col in columns:
            print(f'{col} : {hit.to_dict().get(col)}')


search=Search(index='movies')
query=Fuzzy(影片外国名={'value':'shawshank','fuzziness':0})
query=Fuzzy(影片外国名={'value':'Shawshank','fuzziness':1})
search_query(search,query,columns=['影片中文名'])
