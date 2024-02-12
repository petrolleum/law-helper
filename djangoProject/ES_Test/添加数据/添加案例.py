# import_data.py

import json  # 导入json模块
from django.core.management.base import BaseCommand
from elasticsearch import Elasticsearch
from elasticsearch_dsl import *

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])  # 连接到Elasticsearch
connections.create_connection(hosts=['localhost'])


index_name= "fact"

ik_tokenizer=tokenizer('ik_smart')
ik_analyzer=analyzer('ik_smart',tokenizer=ik_tokenizer)

if Index(index_name).exists():
    Index(index_name).delete()

class Facts(Document):
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
Facts.init()

with open('../../data/fact_test.json', 'r', encoding='utf-8') as file:
    for line in file:
        data = json.loads(line.strip())
        es.index(index='fact', body=data)