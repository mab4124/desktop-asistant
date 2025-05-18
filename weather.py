import requests
from ss import *

api_address = "https://api.openweathermap.org/data/2.5/weather?lat=17.3753&lon=78.4744&appid=1c8c552cd0bxxxxxxxxf04d88e996fc5"
// enter the api id cant share mine
json_data = requests.get(api_address).json()

def temp():
    temperature = round(json_data["main"]["temp"]-273,1)
    return temperature
def des():
    description = json_data["weather"][0]["description"]
    return description

