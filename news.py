import requests
from ss import *
api_address = "https://newsapi.org/v2/everything?q=tesla&from=2024-05-13&sortBy=publishedAt&apiKey=xxxxxeec947848f78158528cb168df05"
// use your own api id
json_data=requests.get(api_address).json()
ar = []

def news():
    for i in range(3):
       ar.append( "number"+ str(i+1) + json_data["articles"][i]["title"] +json_data["articles"][i]["description"]+",")
       
    return ar

