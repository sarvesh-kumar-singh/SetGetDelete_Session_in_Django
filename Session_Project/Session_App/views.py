from django.shortcuts import render

# Create your views here.

def Setsession(request):
    request.session['name']='sarvesh'
    request.session['lname']='kumar'
    return render(request,'student/setsession.html')


def Getsession(request):
    # name=request.session['name']
    name=request.session.get('name')
    lname=request.session.get('lname')
    return render(request,'student/getsession.html',{'name':name},{'lname':lname})


def Delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'student/delsession.html')
