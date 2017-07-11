from django.http import HttpResponse
from django.template import loader

from .models import Camera

def index(request):
    cameras = Camera.objects.all()
    template = loader.get_template('cameradb/index.html')
    context = {
        'cameras': cameras,
    }
    return HttpResponse(template.render(context, request))

def show(request, camera_id):
    camera = Camera.objects.filter(id=camera_id)[0]
    template = loader.get_template('cameradb/show.html')
    context = {
        'camera': camera,
    }
    return HttpResponse(template.render(context, request))

def new(request):
    template = loader.get_template('cameradb/new.html')
    context = {}
    return HttpResponse(template.render(context, request))
