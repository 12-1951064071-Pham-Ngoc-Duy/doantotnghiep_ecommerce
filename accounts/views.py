from django.shortcuts import render
from .forms import RegistrationForm
from .models import Account
from django.http import JsonResponse
from .models import CITY_CHOICES, VILLAGE_CHOICES
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            country = form.cleaned_data['country']
            city = form.cleaned_data['city']
            village = form.cleaned_data['village']
            address = form.cleaned_data['address']
            username = email.split("@")[0]
            user = Account.objects.create_user(first_name=first_name, last_name=last_name, phone_number=phone_number, email=email,username=username, password=password, country=country, city=city, village=village, address=address)
            user.phone_number = phone_number
            user.save()
    else:
        form = RegistrationForm() 
    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)

def login(request):
    return render(request, 'accounts/login.html')

def logout(request):
    return 

def load_cities(request):
    country = request.GET.get('country')
    cities = CITY_CHOICES.get(country, [])
    cities_list = [(city[0], city[1]) for city in cities]
    return JsonResponse({'cities': cities_list})

def load_villages(request):
    city = request.GET.get('city')
    villages = VILLAGE_CHOICES.get(city, [])
    villages_list = [(village[0], village[1]) for village in villages]
    return JsonResponse({'villages': villages_list})