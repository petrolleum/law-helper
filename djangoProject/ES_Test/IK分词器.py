import requests
from elasticsearch_dsl.query import *


def es_ik_word(text,url=None,analyzer='ik_max_word'):
    if not url:
        url='http://localhost:9200/_analyze'
    data={'analyzer':analyzer,"text":text}
    response=requests.post(url,json=data)
    tokens=[token["token"] for token in response.json()['tokens']]
    print(tokens)

es_ik_word(text='你好，我来自江西省上饶市',analyzer='ik_smart')


from elasticsearch_dsl import *
connections.create_connection(hosts=['localhost'])

index_name='movies_ik'

ik_tokenizer=tokenizer('ik_smart')
ik_analyzer=analyzer('ik_smart',tokenizer=ik_tokenizer)

if Index(index_name).exists():
    Index(index_name).delete()

class Movies(Document):
    电影详情链接=Keyword()
    图片链接=Keyword()
    影片中文名=Text(analyzer='ik_smart',search_analyzer=ik_analyzer)
    影片外国名=Text(analyzer='ik_smart',search_analyzer=ik_analyzer)
    评分=Float()
    评价数=Integer()
    概况=Text(analyzer='ik_smart',search_analyzer=ik_analyzer)
    相关信息=Text(analyzer='ik_smart',search_analyzer=ik_analyzer)
    class Index:
        name=index_name
        setting={
            "analysis":{
                "analyzer":{
                    "ik_smart":{
                        "tokenizer":"ik_smart"
                    }
                },
                "search_analyzer":{
                    "ik_smart":{
                        "tokenizer":"ik_smart"
                    }
                },
            }
        }
Movies.init()

import pandas as pd
df_movies=pd.read_csv("../data/豆瓣电影Top250.csv")
for row_no,row in df_movies.iterrows():
    movie=Movies(
        电影详情链接=row.电影详情链接,
        图片链接=row.图片链接,
        影片中文名=row .影片中文名,
        影片外国名=row .影片外国名,
        评分=row.评分,
        评价数=row.评价数,
        概况=row.概况,
        相关信息=row.相关信息
    )
    movie.save()

ik_index=Index(index_name)


def search_query(search,query,columns):
    s=search.query(query)
    response=s.execute()

    for hit in response.hits:
        for col in columns:
            print(f'{col} : {hit.to_dict().get(col)}')


search=Search(index=index_name)
query=MultiMatch(query='韩国',fields=['相关信息','概况'])
search_query(search,query,columns=['影片中文名','相关信息'])