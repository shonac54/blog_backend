from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf  import csrf_exempt
import json
from blog.serializer import RegisterSerializer


# Create your views here.
@csrf_exempt
def userRegister(request):
    if request.method == "POST":
        recieved_data=json.loads(request.body)
        serializer_check=RegisterSerializer(data=recieved_data)
        if serializer_check.is_valid():
            serializer_check.save()
            return HttpResponse(json.dumps({"status":"success"}))
        else:
            return HttpResponse(json.dumps({"status":"failed"}))
            
