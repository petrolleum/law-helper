from elasticsearch_dsl import *
from elasticsearch_dsl.query import *

connections.create_connection(hosts=['localhost'])
search=Search(index='movies')

def search_query(search,term,columns):
    s=search.query(term)
    response=s.execute()

    for hit in response.hits:
        for col in columns:
            print(f'{col} : {hit.to_dict().get(col)}')

term=Term(相关信息='美')
search_query(search,term,columns=['影片中文名','相关信息'])