from django.shortcuts import render
from .models import Operator, DroneShot, Booking, Location, Customer
from django.contrib import messages
import hashlib
from .settings import MESSAGE_STORAGE


# Create your views here.

def register(request):
    method = False
    if request.method == 'POST':
        method = True
    unm = False
    if method and not Operator.objects.filter(name=request.POST.get('username')):
        unm = True
    pas = True
    if method and request.POST.get('password1') != request.POST.get('password2'):
        pas = False
    if unm and pas:
        saverecord = Operator()
        saverecord.name = request.POST.get('username')
        passtr = request.POST.get('password1')
        saverecord.password = hashlib.sha256(passtr.encode()).hexdigest()
        saverecord.email = request.POST.get('email')
        saverecord.access = "NO"
        saverecord.save()
        return render(request, 'droame/homepage.html',{'username': saverecord.name})
    else:
        if not unm:
            messages.warning(request, 'Username already exists!')
        if not pas:
            messages.warning(request, 'Passwords don\'nt match!')
        return render(request, 'droame/register.html', {})


def login(request):
    method = False
    if request.method == 'POST':
        method = True
    unm = True
    if method and not Operator.objects.filter(name=request.POST.get('username')):
        unm = False
    pas = False
    if method and unm:
        opr = Operator.objects.get(name=request.POST.get('username'))
        passtr = request.POST.get('password')
        if opr.password == hashlib.sha256(passtr.encode()).hexdigest():
            pas = True
    if method and unm and pas:
        return render(request, 'droame/homepage.html', {'username': request.POST.get('username')})
    else:
        if not unm:
            messages.warning(request, 'Username doesn\'nt exist!')
        if unm and not pas:
            messages.warning(request, 'Please enter valid password!')
        return render(request, 'droame/login.html', {})


def homepage(request):
    return render(request, 'droame/homepage.html', {})


def forgotPassword(request):
    return render(request, "<h1> Hello </h1>", {})
