from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import City
from .forms import City_Form

# Create your views here.
def weather(request):
		cities=City.objects.all()
		form=City_Form()
		#return HttpResponse(form)
		'''
		To get API-KEY, register at https://home.openweathermap.org/users/sign_in

		'''
		url = 'api.openweathermap.org/data/2.5/weather?q=kochi&units=imperial&appid=YOUR-API-KEY'
		if request.method=='POST':
			form=City_Form(request.POST)
			form.save()

		wdata=[]
		for city in cities:		
			city_weather=requests.get(url. format(city)).json()
			weather_data={'city':city_weather['name'], 'temperature':city_weather['main']['temp'], 'description':city_weather['weather'][0]['description'], 'icon':city_weather['weather'][0]['icon']}
			wdata.append(weather_data)
		context={'weathers': wdata, 'form': form}
		return render(request, 'weather_index.html', context=context)
