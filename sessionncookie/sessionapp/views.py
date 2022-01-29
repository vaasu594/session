from django.shortcuts import render
from django.http import HttpResponse

def input(request):
    return render(request,'base.html')

def add(request):
    if request.method=="POST":
        x=int(request.POST['f'])
        y=int(request.POST['s'])
        z=x+y
        request.session['z']=z
        request.session.set_expiry(60)
        return HttpResponse('data submitted successfully')
    elif request.method=='GET':

        x=int(request.GET['f'])
        y=int(request.GET['s'])
        z=x+y
        request.session['z']=z
        request.session.set_expiry(60)
        return HttpResponse('data submitted successfully')

def display(request):
    if request.session.has_key('z'):
        z=request.session['z']
        return HttpResponse(z)
    else:
        return render(request,'base.html')

        

# Create your views here.
