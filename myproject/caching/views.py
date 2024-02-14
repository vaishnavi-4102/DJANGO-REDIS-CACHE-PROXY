import requests
import json
from django.shortcuts import HttpResponse
from django.core.cache import cache


# Create your views here.
def fetch_cached_data(request):
    api_url = 'https://jsonplaceholder.typicode.com/todos/'
    cached_data = cache.get('key_3')

    
    if cached_data:
        return HttpResponse(cached_data)
    try:
       response = requests.get(api_url)
    
       if response.status_code == 200:
        data = response.json()
        cache.set('key_3', data, timeout=3600)
        # print(cache)
        return HttpResponse(json.dumps(data))
       else:
        return HttpResponse('Failed to fetch data from API', status = response.status_code)
    except Exception as e:
       print(e)
       return HttpResponse(e)
    
def get_cached_keys(request):
    # Retrieve all keys from cache
    keys = cache.keys('*')
    return HttpResponse(keys) 



