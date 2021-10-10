import requests
from time import sleep
from json import dumps
from kafka import KafkaProducer
def free_news_api_request():
    url = "https://free-news.p.rapidapi.com/v1/search"
    querystring = {"q":"Elon Musk","lang":"en"}
    headers = {
        'x-rapidapi-host': "free-news.p.rapidapi.com",
        'x-rapidapi-key': "3cd7e29563mshb99aad2cbc12deap1c2b67jsne491a79b4854"
        }
    response = requests.request("GET", url, headers=headers, params=querystring)
    json_response = response.json()
    articleList = json_response["articles"]
    attributeList = ["title","published_date","link","clean_url","summary","country","language","authors","media","topic"]
    filtered_articleList = []
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x:dumps(x).encode('utf-8'))
   # for i in range(json_response["page_size"]):
   #     json_article = articleList[i]
   #     filteredjson_article = {}
   #     for items in attributeList:
   #         filteredjson_article[items] = json_article[items]
   #     filtered_articleList.append(filteredjson_article)
   # for i in filtered_articleList:
    producer.send("newsarticle",value={"name":"naveen"})