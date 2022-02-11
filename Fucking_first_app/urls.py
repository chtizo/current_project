# from django.urls import path
# from . import views
# urlpatterns =  [
#    path('', views.index)
# ]



from django.contrib import admin  
from django.urls import path  
from Fucking_first_app import views  
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('', views.index),  
]  