from elasticsearch_dsl import *
from elasticsearch_dsl.query import Regexp, Query

connections.create_connection(hosts=['localhost'])

def search_query(search,query,columns):
    s=search.query(query)
    response=s.execute()

    for hit in response.hits:
        for col in columns:
            print(f'{col} : {hit.to_dict().get(col)}')


search = Search(index='movies')
query= Regexp(相关信息='驰')
search_query(search,query,columns=['影片中文名','相关信息'])