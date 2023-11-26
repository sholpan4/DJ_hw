from django.shortcuts import render
import requests
import json


def get_data_from_api(request):
    api_url = 'https://jsonplaceholder.typicode.com/todos/'
    response = requests.get(api_url)
    data = response.json()

    with open('api_data.json', 'w') as json_file:
        json.dump(data, json_file)
    print(data)

    return render(request, 'show_data.html', {'data': data})