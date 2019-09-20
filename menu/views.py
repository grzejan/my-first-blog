from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def item_list(request):
    uris=[]
    uris.append(['grzejan blog', '/blog/'])
    uris.append(['echo (a=111, b=ala mak ota, c=232)', '/echo/?a=111&b=ala mak ota&c=232'])
    uris.append(['Starpusher', '/starpusher/'])
    return render(request, 'menu/item_list.html', {'uris':uris})

@csrf_exempt
def echo(request):
    resp = "Echo:<br>"
    resp += 'user.is_authenticated: '+str(request.user.is_authenticated)+'<br>'
    resp += 'CSRF_COOKIE: '+str(request.META['CSRF_COOKIE'])+'<br>'
    if request.method == 'GET':
        resp+="GET<br>"
        resp+=str(list(request.GET.items()))+'<br>'
    elif request.method == 'POST':
        resp+="POST<br>"
        resp +=str(list(request.POST.items()))+'<br>'
    resp += '<br>'+str(list(request.META.items()))+'<br>'
    return HttpResponse(resp)