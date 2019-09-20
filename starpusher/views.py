from django.shortcuts import render, redirect

# Create your views here.
def starpusher(request):
   return render(request, 'starpusher.html', {})
#    return redirect('starpusher')