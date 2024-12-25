"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import index

from django.http import HttpResponse

def home(request,a,b):
    print(a,b)
    c = a+b
    return HttpResponse(f"<h1>{a}+{b}={c}</h1>")

def count(request,matn):
    harf = 0
    son = 0
    for i in matn:
        if str(i).isalpha():
            harf = harf+1
        elif str(i).isdigit():
            son = son +1
    return HttpResponse(f"<h1>harflar: {harf}\n sonlar {son}</h1>")

def search(request,matn):
    return HttpResponse(f"<a href='http://google.com/search?q={matn}' class='button'>Go to Google</a>")

    
import google.generativeai as genai
def make_conver(request,text):
    genai.configure(api_key="AIzaSyAW2brzIdnFsLWJDk68viWgPNl0N08ZwTY")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(text)
    return HttpResponse(response.text)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('<int:a>/<int:b>/',home),
    # path("<str:matn>/",count),
    path('qidiruv/<str:matn>/',search),
    path('jimini/<str:text>/',make_conver),
    path('index/',index)
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
