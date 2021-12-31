from typing import Text
import requests
import json





class Weather():
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Kharar,Punjab&appid=af17c2487cdd8e022202ae9bdd7da175")

    def sorters(obj):
        print(Weather.response.status_code) #gets the response code 
        text = json.dumps(obj, sort_keys=True , indent=3)
        print(str(text)) 
        
        
class News():
    response = requests.get("https://newsapi.org/v2/everything?q=Apple&+from=2021-12-28&sortBy=popularity&apiKey=4f391d28e0c1407b9e01ef63ce55cdb4")

    def sorters_news(obj):
        print(News.response.status_code)
        Text = json.dumps(obj , sort_keys=True , indent=4)
        print(str(Text))