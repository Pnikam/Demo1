
from django.http import HttpResponse
from django.shortcuts import render
import requests, json
import pgeocode

def index(request):
    return render(request, 'index.html')

    #return HttpResponse('''<h1>Welcome!</h1> <a href = "https://www.geeksforgeeks.org/">GeeksforGeeks</a>''')

def report(request):
    # Get the text

    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city = request.GET.get('city', 'default')
    api_key = "c6ad51f2ce3ecf827e9b9e42059dc8ee"
    URL = base_url + "appid=" + api_key + "&q=" + city
    response = requests.get(URL)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]
        temp = str(round(y["temp"]-273.15,2))
        pres = str(y["pressure"])
        hum = str(y["humidity"])
        weather = str(x["weather"][0]["description"])
        params = {'name': city, 'temp': temp, 'pressure': pres , 'humidity': hum, 'weather': weather}
        return render(request, 'report.html', params)

    else:
        return HttpResponse("Error")
