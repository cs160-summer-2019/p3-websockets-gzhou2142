from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, 'draw/index.html', {})

def variant(request):
    return render(request, 'draw/variant.html', {})
  
# def room(request, room_name):
#     return render(request, 'draw/room.html', {
#         'room_name_json': mark_safe(json.dumps(room_name))
#     })