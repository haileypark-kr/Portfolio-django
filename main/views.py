from django.shortcuts import render
from main.models import Project
from django.conf import settings
from django.http import HttpResponse
import os
# Create your views here.

def view_projects(request):
    posts = Project.objects.order_by('startdate')
    return render(request, 'projects.html', {'posts':posts.reverse()})

def download(request,file_name):
    file_path = os.path.join(settings.MEDIA_ROOT,file_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response

def index(request):
    return render(request,'index.html')
