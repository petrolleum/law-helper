import json
import os
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from elasticsearch_dsl import *
from elasticsearch_dsl.query import *

from djangoProject import settings

connections.create_connection(hosts=['localhost'])

total_hits=0

def search_query(search,query,columns):
    s=search.query(query)
    response=s.execute()

    for hit in response.hits:
        for col in columns:
            print(f'{col} : {hit.to_dict().get(col)}')



def law_query(request):
    if request.method == 'POST':
        law_number = request.POST.get('law_number', '')
        law_content = request.POST.get('law_content','')
        fact_content = request.POST.get('fact_content','')
        # search = Search(index='law')
        # query = Match(num=law_number)
        if law_content:
            search = Search(index='law')
            query= Match(content=law_content)
        if law_number:
            search = Search(index='law')
            query = Match(num=law_number)
        if fact_content:
            search = Search(index='fact')
            query=Match(fact=fact_content)
        response = search.query(query).execute()
        results=response.hits
        print(results[0]['meta'])
        for key in results[0].meta:
            print(key+":")
        return render(request, 'law_result.html',{'results':results})
    return render(request, 'law_query.html')


def judgement_query(request):
    if request.method == 'POST':
        judgement_content = request.POST.get('judgement_content','')
        # search = Search(index='judgement')
        # query = Match(num=judgement_number)
        if judgement_content:
            search = Search(index='judgement')
            query= Match(content=judgement_content)
            response = search.query(query).execute()
            results=response.hits
            return render(request, 'judgement_result.html',{'results':results})
    return render(request, 'judgement_query.html')



def getImageByUrl(request,image_name):
    image_path =settings.STATIC_MEDIA+"/img/"+image_name

    print("url"+image_path)

    if os.path.exists(image_path):
        with open(image_path, 'rb') as f:
            return HttpResponse(f.read(), content_type='image/jpeg')  # 假设图片是 JPEG 格式的
    else:
        return HttpResponse('Image not found', status=404)


def getLawByNum(request):
    if request.method=="POST":
        request_data = json.loads(request.body)
        lawNum = request_data.get("lawNum")
        search = Search(index='law')
        lawList=[]
        if lawNum:
            for i in range(int(lawNum), int(lawNum) + 10):
                query = Match(num=i)
                response = search.query(query).execute()
                results = response.hits
                print(results)
                tmp={'num':results[0].num,'content':results[0].content}
                lawList.append(tmp)
            response = JsonResponse({'law':json.dumps(lawList)})
            response['Access-Control-Allow-Origin'] = '*'
            return response
        else:
            response = JsonResponse({'error':'错误'})
            response['Access-Control-Allow-Origin'] = '*'
            return response

def getLawByContent(request):
    if request.method=="POST":
        request_data = json.loads(request.body)
        lawContent = request_data.get("lawContent")
        search = Search(index='law')
        lawList=[]
        if lawContent:
            query = Match(content=lawContent)
            response = search.query(query).execute()
            results = response.hits
            if results:
                for result in results:
                    tmp = {'num': result.num, 'content': result.content}
                    lawList.append(tmp)
                response = JsonResponse({'law': json.dumps(lawList)})
                response['Access-Control-Allow-Origin'] = '*'
                return response
            else:
                response = JsonResponse({'error': "未找到相关法条"})
                response['Access-Control-Allow-Origin'] = '*'
                return response
        else:
            response = JsonResponse({'error':'错误'})
            response['Access-Control-Allow-Origin'] = '*'
            return response

def getFactByKeyWords(request):
    if request.method=='POST':
        request_data = json.loads(request.body)
        factContent = request_data.get("fact_content")
        search = Search(index='fact')
        lawList=[]
        if factContent:
            query = Match(fact=factContent)
            response = search.query(query).execute()
            results = response.hits
            if results:
                print(len(results))
                for result in results:
                    term_of_imprisonment=''
                    if result['meta']['term_of_imprisonment']['death_penalty'] == True:
                        term_of_imprisonment='death'
                    elif result['meta']['term_of_imprisonment']['life_imprisonment'] == True:
                        term_of_imprisonment='life-imprisonment'
                    else:
                        term_of_imprisonment=str(result['meta']['term_of_imprisonment']['imprisonment'])

                    tmp={'content':result.fact,
                         'relevant_articles':json.dumps(list(result['meta']['relevant_articles'])),
                         'accusation':json.dumps(list(result['meta']['accusation'])),
                         'punish_of_money':result['meta']['punish_of_money'],
                         'term_of_imprisonment':term_of_imprisonment
                         }
                    lawList.append(tmp)
                    print(lawList)
                response = JsonResponse({'fact': json.dumps(lawList)})
                response['Access-Control-Allow-Origin'] = '*'
                return response
            else:
                response = JsonResponse({'error': "未找到相关案例"})
                response['Access-Control-Allow-Origin'] = '*'
                return response
        else:
            response = JsonResponse({'error':'错误'})
            response['Access-Control-Allow-Origin'] = '*'

def getJudgements(request):
    if(request.method=='POST'):
        request_data = json.loads(request.body)
        judgement_type=request_data.get('caseType')
        curPage=request_data.get('page')
        searchContent=request_data.get('searchContent')
        judgement_list=[]

        if judgement_type!='bySearch' and judgement_type:
            query = Match(caseType=judgement_type)
            response=Search(index="judgement").query(query).extra(size=10,from_=10*(curPage)).execute()

            results=response.hits
            total_hits = results.total.value
            if results:
                print(results[0]['caseReason'])
                for result in results:
                    reference=result.reference.split('；')
                    caseReason=result.caseReason.split('、')
                    tmp={'id':result.id,
                         'caseTitle':result.caseTitle,
                         'caseId':result.caseId,
                         'court':result.court,
                         'caseType':result.caseType,
                         'proceeding':result.proceding,
                         'reference':json.dumps(reference),
                         'caseReason':json.dumps(caseReason),
                         'judgementTime':result.judgementTime
                         }
                    judgement_list.append(tmp)
                response = JsonResponse({'judgements': json.dumps(judgement_list),'total':total_hits})
                print(len(results))
                response['Access-Control-Allow-Origin'] = '*'
                return response
        elif judgement_type=='bySearch':
            print(11111111111)
            query = Match(caseReason=searchContent)
            response = Search(index="judgement").query(query).extra(size=10, from_=10 * (curPage)).execute()

            results = response.hits
            total_hits = results.total.value
            if results:
                print(results[0]['caseReason'])
                print(results[0]['caseTitle'])
                for result in results:
                    reference = result.reference.split('；')
                    caseReason = result.caseReason.split('、')
                    tmp = {'id': result.id,
                           'caseTitle': result.caseTitle,
                           'caseId': result.caseId,
                           'court': result.court,
                           'caseType': result.caseType,
                           'proceeding': result.proceding,
                           'reference': json.dumps(reference),
                           'caseReason': json.dumps(caseReason),
                           'judgementTime': result.judgementTime
                           }
                    judgement_list.append(tmp)
                response = JsonResponse({'judgements': json.dumps(judgement_list), 'total': total_hits})

                response['Access-Control-Allow-Origin'] = '*'
                return response
    response = JsonResponse({'error': "未找到相关案例"})
    response['Access-Control-Allow-Origin'] = '*'
    return response

def getJudgement(request):
    if request.method=='POST':
        request_data = json.loads(request.body)
        id=request_data.get('id')
        if id:
            query=Match(id=id)
            response=Search(index='judgement').query(query).execute()
            result=response.hits[0]
            reference = result.reference.split('；')
            caseReason = result.caseReason.split('、')

            if result.content.find('审判长')!=-1 :
                content_all = result.content.split('审判长')
                print(content_all)
                content = content_all[0]
                judge = content_all[1]

                if judge.find('更多数据') != -1:
                    judge = judge.split('更多数据')[0]
                elif judge.find('来源') != -1:
                    judge = judge.split('来源')[0]
                elif judge.find('来自') != -1:
                    judge = judge.split('来自')[0]
                elif judge.find('微信公众号') != -1:
                    judge = judge.split('微信公众号')[0]
                elif judge.find('搜索') != -1:
                    judge = judge.split('搜索')[0]
            elif result.content.find('审 判 长')!=-1:
                content_all = result.content.split('审判员')
                print(content_all)
                content = content_all[0]
                judge = content_all[1]

                if judge.find('更多数据') != -1:
                    judge = judge.split('更多数据')[0]
                elif judge.find('来源') != -1:
                    judge = judge.split('来源')[0]
                elif judge.find('来自') != -1:
                    judge = judge.split('来自')[0]
                elif judge.find('微信公众号') != -1:
                    judge = judge.split('微信公众号')[0]
                elif judge.find('搜索') != -1:
                    judge = judge.split('搜索')[0]
            elif result.content.find('审判员')!=-1:
                content_all = result.content.split('审判员')
                print(content_all)
                content = content_all[0]
                judge = content_all[1]

                if judge.find('更多数据') != -1:
                    judge = judge.split('更多数据')[0]
                elif judge.find('来源') != -1:
                    judge = judge.split('来源')[0]
                elif judge.find('来自') != -1:
                    judge = judge.split('来自')[0]
                elif judge.find('微信公众号') != -1:
                    judge = judge.split('微信公众号')[0]
                elif judge.find('搜索') != -1:
                    judge = judge.split('搜索')[0]
            else:
                content=result.content
                judge=''

            response=JsonResponse({'id':result.id,
                                   'caseTitle':result.caseTitle,
                                   'caseId':result.caseId,
                                   'court':result.court,
                                   'judgementTime':result.judgementTime,
                                   'caseType':result.caseType,
                                   'proceeding':result.proceding,
                                   'reference': json.dumps(reference),
                                   'caseReason': json.dumps(caseReason),
                                   'content':content,
                                   'judge':judge
                                   })
            response['Access-Control-Allow-Origin'] = '*'
            return response









