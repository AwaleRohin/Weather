import requests
from django.shortcuts import render, get_object_or_404, redirect
from .models import City
from .forms import CityForm

# Create your views here.


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=e298815beff36df9b1e0b99a4f4f54db'
    weather_data = []

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all().order_by('-created_at')
    for city in cities:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'id': city.id,
            'city': city,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon']
        }
        weather_data.append(city_weather)

    args = {'weather_data': weather_data, 'form': form, 'city': cities}
    return render(request, 'weather.html', args)


def delete_city(request, pk):
    city = get_object_or_404(City, id=pk)
    city.delete()
    return redirect('index')
