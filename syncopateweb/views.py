from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render

def showcluster(request, url):
    url = url.replace('/','')
    print(url)
    keys = url.split('&')
    serieskeys = []
    for k in keys:
        tokens = k.split('.')
        if len(tokens) >= 2:
            serieskeys.append(tokens[1])
    wspath = '&'.join([ 'series=%s' % k for k in keys ])
    wshost = 'api.blub.io:32790'
    wsurl = "ws://%s/ws?%s" % (wshost, wspath);
    print(wsurl)
    context = { 
        'urlpath' : url,
        'wsurl'   : wsurl,
        'serieskeys' : serieskeys,
        }
    #return HttpResponse(url)
    return render(request, 'syncopateweb/index.html', context)
