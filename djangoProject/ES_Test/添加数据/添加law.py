import requests
from elasticsearch_dsl.query import *
from elasticsearch_dsl import *

connections.create_connection(hosts=['localhost'])

index_name= "law"

ik_tokenizer=tokenizer('ik_smart')
ik_analyzer=analyzer('ik_smart',tokenizer=ik_tokenizer)

if Index(index_name).exists():
    Index(index_name).delete()

class Laws(Document):
    num=Keyword()
    content=Text(analyzer='ik_smart',search_analyzer=ik_analyzer)
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
Laws.init()

import pandas as pd
df_movies=pd.read_csv("../../data/CriminalLaw.csv")
for row_no,row in df_movies.iterrows():
    law=Laws(
        num=row.num,
        content=row.处理后内容,
    )
    law.save()

ik_index=Index(index_name)
