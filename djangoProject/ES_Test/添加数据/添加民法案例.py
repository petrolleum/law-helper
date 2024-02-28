import requests
from elasticsearch_dsl.query import *
from elasticsearch_dsl import *

connections.create_connection(hosts=['localhost'])

index_name= "judgement"

ik_tokenizer=tokenizer('ik_smart')
ik_analyzer=analyzer('ik_smart',tokenizer=ik_tokenizer)

if Index(index_name).exists():
    Index(index_name).delete()

class Laws(Document):
    id = Integer()
    caseTitle = Text(analyzer='ik_smart',search_analyzer=ik_analyzer)
    caseId = Keyword()
    court = Text(analyzer='ik_smart',search_analyzer=ik_analyzer)
    caseType = Text(analyzer='ik_smart',search_analyzer=ik_analyzer)
    proceding = Text(analyzer='ik_smart',search_analyzer=ik_analyzer)
    reference = Text(analyzer='ik_smart',search_analyzer=ik_analyzer)
    content = Text(analyzer='ik_smart',search_analyzer=ik_analyzer)
    caseReason = Text(analyzer='ik_smart', search_analyzer=ik_analyzer)
    judgementTime = Keyword()
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

num=0
import pandas as pd
df_judgement=pd.read_csv("E:\BaiduNetdiskDownload\judgement.csv")
for row_no,row in df_judgement.iterrows():
    if pd.notna(row.案件名称) and pd.notna(row.案号) and pd.notna(row.法院) and pd.notna(row.案件类型) and pd.notna(row.审理程序) and pd.notna(row.法律依据)and pd.notna(row.案由)and pd.notna(row.全文):
        law=Laws(
        id=num,
        caseTitle=row.案件名称,
        caseId=row.案号,
        court=row.法院,
        caseType=row.案件类型,
        proceding=row.审理程序,
        reference=row.法律依据,
        caseReason=row.案由,
        content=row.全文,
        judgementTime="2021年8月",
        )
        num+=1
        law.save()


