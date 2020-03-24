from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import os
import json
import requests as request_python
# Create your views here.
def index(request):
    return HttpResponse('Ola, pagina index de API')

def get_results_by_search(request, title):
    req = request_python.get(f'http://www.omdbapi.com/?apikey={os.getenv("key_movie_database")}&s={title.replace(" ", "+")}')

    if req.status_code == 200:
        return JsonResponse(json.loads(req.text))
    return JsonResponse({'Response':'False'})

def get_information_movie(request, id_movie):
    req = request_python.get(f'http://www.omdbapi.com/?apikey={os.getenv("key_movie_database")}&plot=full&i={id_movie}')

    if req.status_code == 200:
        return JsonResponse(json.loads(req.text))
    return JsonResponse({'Response':'False'})

def watch_movie(request, id_movie):
    return JsonResponse({"link":f"https://videospider.stream/personal?key={os.getenv('key_video_spider')}&video_id={id_movie}"})
