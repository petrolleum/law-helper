from elasticsearch_dsl import *

connections.create_connection(hosts=['localhost'])

search=Search(index='movies')
query=Q('match',相关信息="冒险")
s=search.query(query)
response=s.execute()
for hit in response.hits:
    print(f'影片中文名 {hit.影片中文名}')
    if(hit.影片外国名!=''):
        print(f'影片外国名 {hit.影片外国名}')
    print(f'评分 {hit.评分}')
    print(f'概况 {hit.概况}')
    print(f'相关信息 {hit.相关信息}')

# 同时进行多个查询
ms=MultiSearch(index='movies')
s1=Search()
s1=s1.query('match',相关信息="童话")
ms=ms.add(s1)

s2=Search()
s2=s2.query('match',概况="童话")
ms=ms.add(s2)

responses=ms.execute()
for response in responses:
    for hit in response.hits:
        print(hit.影片中文名)

