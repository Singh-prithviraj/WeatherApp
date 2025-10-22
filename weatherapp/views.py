from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

# Create your views here.
def home(request):

    if 'city' in request.POST:
        city = request.POST.get('city')
    else: 
        city = 'indore' 

    url = f' https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2ae11e0db6a16eb58dfbaee44cc4086f'
    
    para = {'units':'metric'}
 
    API_KEY = 'AIzaSyBFUUZOPd3wvjO7mQ-1kgoLO8mzJVQB5lw'
    SEARCH_ENGINE_ID = 'b2c81c2c05e8645ce'

    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    data = requests.get(city_url).json()
    count = 1
    search_items = data.get("items")
    image_url = search_items[1]['link']
    try:
        data = requests.get(url,params = para).json()

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

        day = datetime.date.today()


        return render(request, 'weatherapp/index.html',{'description': description,'icon':icon,'temp':temp,'day':day,'city':city,'exception_occurred': False,'image_url': image_url})
    except:
        exception_occurred=True
        messages.error(request,'entered data is not available to API')
        day=datetime.date.today()

        return render(request, 'weatherapp/index.html',{'description':'clear sky','icon':'01d','temp':25,'day':day,'city':'indore','exception_occurred': True})
