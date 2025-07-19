from django.shortcuts import render
import requests
import json


def index(request):
    public_ip = requests.get('https://api.ipify.org?format=json').json()['ip']
    res = requests.get(f'http://ip-api.com/json/{public_ip}')
    location_data_one = res.text
    location_data = json.loads(location_data_one)
    return render(request, 'index.html', {'data': location_data})