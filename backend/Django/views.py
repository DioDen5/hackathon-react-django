# Django/views.py
from django.http import JsonResponse

def hello_world(request):
    data = {'message': 'Hello, World!'}
    return JsonResponse(data)
