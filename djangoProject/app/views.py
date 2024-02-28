import json
import os
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from elasticsearch_dsl import *
from elasticsearch_dsl.query import *

from djangoProject import settings

connections.create_connection(hosts=['localhost'])

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

<<<<<<< HEAD
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


=======
def getImageByUrl(request,image_name):
    image_path =settings.STATIC_MEDIA+"/img/"+image_name

    print("url"+image_path)

    if os.path.exists(image_path):
        with open(image_path, 'rb') as f:
            return HttpResponse(f.read(), content_type='image/jpeg')  # 假设图片是 JPEG 格式的
    else:
        return HttpResponse('Image not found', status=404)
>>>>>>> 1e0477ef07e0311f6c99431759115dfc5863e59e

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






