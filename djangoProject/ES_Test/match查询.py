from elasticsearch_dsl import *
from elasticsearch_dsl.query import *

connections.create_connection(hosts=['localhost'])

def search_query(search,query,columns):
    s=search.query(query)
    response=s.execute()

    for hit in response.hits:
        for col in columns:
            print(f'{col} : {hit.to_dict().get(col)}')


search = Search(index='movies')
#query=Match(影片中文名='霸王别姬')
#query=MatchAll()
#query=MatchPhrase(影片中文名='霸王别姬')
#query=MatchPhrasePrefix(相关信息='Nolan')
query=MatchBoolPrefix(相关信息='Nolan')&Match(相关信息='惊悚')
search_query(search,query,columns=['影片中文名','相关信息'])
print("------------")

query=MultiMatch(query='韩国',fields=['相关信息','概况'])
search_query(search,query,columns=['影片中文名','相关信息'])
print("------------")
query=MultiMatch(query='韩国',fields=['相关信息','概况'],minimum_should_match=2)
search_query(search,query,columns=['影片中文名','相关信息'])