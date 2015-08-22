from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render

def showcluster(request, url):
    print(url)
    context = { 'urlpath' : url }
    #return HttpResponse(url)
    return render(request, 'syncopateweb/index.html', context)
