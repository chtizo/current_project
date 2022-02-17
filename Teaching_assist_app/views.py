# from django.shortcuts import render
# from .models import Video

# # Create your views here.
# def index(request):
#     video=Video.objects.all()
#     return render(request,"index.html",{"video":video})
# # Create your views here.

file = ''
from importlib.machinery import SourceFileLoader
location = "Teaching_assist_app/Drowsiness_detect/yolov5/"
detect = SourceFileLoader("Detect_uploaded_video",location + "Detect_uploaded_video.py").load_module()


from contextlib import nullcontext
import json
from time import sleep
from django.shortcuts import render  
from django.http import HttpResponse  
from django.http import StreamingHttpResponse  
from django.http import JsonResponse
from torch import rand  
from Teaching_assist_app.functions import handle_uploaded_file  
from Teaching_assist_app.forms import VideoForm  
from Teaching_assist_app.forms import AnalyseConfirm  
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
            
            link = 'Teaching_assist_app/upload/' + file
            return StreamingHttpResponse(detect.detection(link, location))
            # return StreamingHttpResponse(iterator())
    else:  
        video = VideoForm()  
        analyse = AnalyseConfirm()
        return render(request,"index.html",{'video':video, 'analyse': analyse})  

def iterator():
    x = 100
    y = 0
    total = x
    fps = 30
    while (x > 0):
        y += 1
        x -= 1
        time = y/fps
        total_time = total/fps
        sleep(0.1)
        out = {
            "time": time,
            "total_time": total_time,
            "current_frame": y,
            "total_frames": total,
            "awake": random.randint(0, 100),
            "drowsy": random.randint(0, 100),
            "happy": random.randint(0, 100),
            "stressed": random.randint(0, 100),
            "fps": fps
        }
        yield json.dumps(out) + '|'