# from django.shortcuts import render
# from .models import Video

# # Create your views here.
# def index(request):
#     video=Video.objects.all()
#     return render(request,"index.html",{"video":video})
# # Create your views here.

file = ''
from importlib.machinery import SourceFileLoader
location = "C:/Users/PAVILION/AppData/Local/Programs/Python/Python37/Drowsiness_detect/yolov5/"
detect = SourceFileLoader("Detect_uploaded_video",location + "Detect_uploaded_video.py").load_module()


from contextlib import nullcontext
import json
from time import sleep
from django.shortcuts import render  
from django.http import HttpResponse  
from django.http import StreamingHttpResponse  
from django.http import JsonResponse
from torch import rand  
from Fucking_first_app.functions import handle_uploaded_file  
from Fucking_first_app.forms import VideoForm  
from Fucking_first_app.forms import AnalyseConfirm  
import random
from django.conf import settings



def index(request):  
    global x
    if request.method == 'POST':  
        global file
        if (request.POST['ins'] == 'upload'):
            
            path = handle_uploaded_file(request.FILES['file'])  
            file = request.FILES['file']._name
            print(file)
            return HttpResponse('uploaded|' + path)  
        elif (request.POST['ins'] == 'analyse'):
            
            link = 'C:/Users/PAVILION/AppData/Local/Programs/Python/Python37/Teaching/current_project/Fucking_first_app/upload/' + file
            return StreamingHttpResponse(detect.detection(link, location))
            # return StreamingHttpResponse(iterator())
    else:  
        video = VideoForm()  
        analyse = AnalyseConfirm()
        return render(request,"index.html",{'video':video, 'analyse': analyse})  

def iterator():
    x = 50
    y = 0
    total = x
    while (x > 0):
        y += 1
        x -= 1
        sleep(0.05)
        out = {
            "current": y,
            "total": total,
            "value": random.randint(10, 30)
        }
        yield json.dumps(out) + '|'