from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    api_url = "https://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&units=metric&q="
    city_name = "Egypt"

    url =api_url + city_name

    response = requests.get(url)
    content = response.json()

    temperature_c = round(content['main']['temp'], 1)
    temperature_f = round((temperature_c * 9 / 5) + 32, 1)

    city_weather = {
        'city':city_name,
        'temperature_c': temperature_c,
        'temperature_f': temperature_f,
        'description': content['weather'][0]['description'],
        'icon': content['weather'][0]['icon'],
    }

    return render(request, 'weather.html', {'city_weather': city_weather})