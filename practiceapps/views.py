from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import usersForm
from service.models import Service
from django.core.paginator import Paginator

def homePage(request) :
    serviceData=Service.objects.all()
    data = {
        'serviceData' : serviceData
    }
    return render(request, "index.html", data)

def aboutUs(request) :
    if request.method=="GET" :
        output = request.GET.get("output")
    return render(request,"about.html", {"output" : output})

def course(request) :
    return HttpResponse('Course')

# Integer
def courseDetails(request, courseid) :
    return HttpResponse(courseid)

# String based
def courseDetailsStr(request, coursedet) :
    return HttpResponse(coursedet)

# Slug based
def courseDetailsSlug(request, courseslug) :
    return HttpResponse(courseslug)

# Random
def courseDetailsRand(request, courserand) :
    return HttpResponse(courserand)

def userForm(request) :
    fn=usersForm()
    data = {"forms":fn}
    return render(request, "userform.html", data)

def submitform(request) :
    sol =0
    fn=usersForm()
    data = {"forms":fn}
    try :
        if request.method=="POST" :
            n1 = int(request.POST.get("num1"))
            n2 = int(request.POST.get("num2"))
            sol = n1 + n2
            data = {
                "forms": fn,
                "n1" : n1,
                "n2" : n2,
                "output" : sol
            }
            return HttpResponse(sol)
    except :
        pass

def evenodd(request) :
    c =''
    if request.method=="POST" :
        n = int(request.POST.get("num1"))
        if(n%2==0) :
            c = 'Even Number'
        else :
            c = 'Odd Number'
    fn=usersForm()
    data = {
        "forms":fn,
        "output":c
    }
    return render(request, "evenodd.html",data)

def marksheet(request) :
    sum = 0
    per = 0.0
    c = ''
    if request.method=="POST" :
        n1 = int(request.POST.get("num1"))
        n2 = int(request.POST.get("num2"))
        n3 = int(request.POST.get("num3"))
        n4 = int(request.POST.get("num4"))
        n5 = int(request.POST.get("num5"))
        sum = n1+n2+n3+n4+n5
        per = sum/5
        if per>60 :
            c = 'First Div'
        elif per > 48 :
            c = 'Second Div'
        elif per>35 :
            c = 'Third Div'
        else :
            c = 'Failed'
    fn = usersForm()
    data = {
        "forms" : fn,
        "total" : sum,
        "perc" : per,
        "div" : c
    }
    return render(request, "marksheet.html", data)