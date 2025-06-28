from django.shortcuts import render , HttpResponse
from django.contrib import messages
import requests
import datetime
# Create your views here.
def home(request):

    if request.method == 'POST':
        city = request.POST['city']
    else:
        city = 'Lahore'     

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a6fbccee449ee9714daf621e9ad8bf2a'
    PARMS = {'units':'metric'}


    data = requests.get(url,PARMS).json()
    
    try:
        desc = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']
        day = datetime.date.today()
        latitude = data['coord']['lat']
        londgitude = data['coord']['lon']

        contxt = { 
        
        'city':city, 
        'desc':desc, 
        'icon':icon, 
        'temp':temp, 
        'day' :day , 
    
    }
        return render(request, 'home.html',contxt)
   
    except:
        Exp = True 
         
        context = {
            
        'Exp':Exp,     

        }
        messages.error(request, 'city not available')
        return render(request, 'home.html',context)

    
    
    
    
    
