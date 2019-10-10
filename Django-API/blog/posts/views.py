from django.shortcuts import render
from .api.views import *
# Create your views here.

# def Dashboard(request):
#     print(PostCreateView.serializer_class)
#     return render(request,'index.html')


##  http://127.0.0.1:8006/api/v1/posts/create/        --> Create
##  http://127.0.0.1:8006/api/v1/posts/1/             --> POST