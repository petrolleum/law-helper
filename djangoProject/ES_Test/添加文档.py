from elasticsearch_dsl import *

connections.create_connection(hosts=['localhost'])
index = Index('movies')

class Movies(Document):
    电影详情链接=Keyword()
    图片链接=Keyword()
    影片中文名=Text()
    影片外国名=Text()
    评分=Float()
    评价数=Integer()
    概况=Text()
    相关信息=Text()
    class Index:
        name="movies"

if Index("movies").exists():
    Index("movies").delete()

import pandas as pd
df_movies = pd.read_csv("../data/豆瓣电影Top250.csv")
data=df_movies.iloc[0,:]
movie=Movies(
    电影详情链接=data.电影详情链接,
    图片链接=data.图片链接,
    影片中文名=data.影片中文名,
    影片外国名=data.影片外国名,
    评分=data.评分,
    评价数=data.评价数,
    概况=data.概况,
    相关信息=data.相关信息
)
for row_no,row in df_movies.iterrows():
    movie=Movies(
        电影详情链接=row.电影详情链接,
        图片链接=row.图片链接,
        影片中文名=row.影片中文名,
        影片外国名=row.影片外国名,
        评分=row.评分,
        评价数=row.评价数,
        概况=row.概况,
        相关信息=row.相关信息
        )
    movie.save()