from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import os
import json
# Create your views here.
def index(request):
    return HttpResponse('Ola, está e pagina index de Data-access. ' + os.getenv('name_env'));

def jsonTest(request):
    return JsonResponse({'foo':'bar'})

#@csrf_exempt
def recebendoJson(request):
    received_json = json.loads((request.body).decode('utf-8'))

    string = ''
    for x in received_json:
        string += received_json[x] + '<br>'

    return HttpResponse('Data: ' + '<br>' + string);
