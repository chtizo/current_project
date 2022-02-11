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
from json import JSONEncoder
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

def index(request):  
    global x
    if request.method == 'POST':  
        global file
        if (request.POST['ins'] == 'upload'):
            
            handle_uploaded_file(request.FILES['file'])  
            file = request.FILES['file']._name
            print(file)
            return HttpResponse('uploaded')  
        elif (request.POST['ins'] == 'analyse'):
            
            link = 'C:/Users/PAVILION/AppData/Local/Programs/Python/Python37/Fucking_first(2)/Fucking_first/Fucking_first_app/upload/' + file
            return StreamingHttpResponse(detect.detection(link, location))
            # return StreamingHttpResponse(iterator())
    else:  
        video = VideoForm()  
        analyse = AnalyseConfirm()
        return render(request,"index.html",{'video':video, 'analyse': analyse})  

def iterator():
    x = 20
    y = 0
    total = x
    while (x > 0):
        y += 1
        x -= 1
        sleep(0.05)
        yield '{"current": "' + str(y) + '", "total": "' + str(random.randint(10, 30)) + '"}|'