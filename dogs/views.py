import requests
from django.shortcuts import render

def get_dogs(request):
    response = requests.get('https://dog.ceo/api/breeds/image/random')
    dog = response.json()['message']
    context = {
        'dog': dog
    }
    return render(request, 'dogs.html', context)