from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.contrib.auth import logout
from Property.models import property

# Create your views here.

def index(request):
    user_=User.objects.filter(username=request.user)
    #agent_=agent.objects.get(username=request.user)
    if user_:
        data={
            'agent':False
        }
        return render(request,'index.html',{'data':data})
    else:
        return render(request,'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        password = request.POST.get('Password')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return render(request,'index.html')
        else:
            return HttpResponse("User Not Exist ")
    else:
        return render(request, 'Login.html', )

def logout(request):
    auth.logout(request)
    return render(request,'index.html')

def createnewacc(request):
    if request.method=="POST":
        first_name=request.POST.get('Firstname')
        last_name=request.POST.get('Lastname')
        username = request.POST.get('Uname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')
        if pass1==pass2:
            user=User.objects.create_user(username=username,password=pass1,first_name=first_name,last_name=last_name,email=email)
            user.save()
            print(first_name,last_name,username,email,pass1,pass2)
            return render(request,'index.html')
        else:
            return HttpResponse("Password Does not Match ...")
    else:
        return HttpResponse('NO ..')
def profile(request):
    user=User.objects.get(username=request.user)
    return render(request,'profile.html',{'user':user})

def searchbycity(request):
    if request.method=="POST":
        type_ = request.POST.get('city')
        print(type_)
        result=property.objects.filter(city=type_)
        if result:
            return render(request,'property-grid.html',{'data':result})
        else:
            return HttpResponse(" <h1> No Result Found</h1> ")
    else:
        return HttpResponse(" <h1> Denial </h1>")

def searchbytype(request):
    if request.method=="POST":
        type_ = request.POST.get('type')
        print(type_)
        result=property.objects.filter(type=type_)
        if result:
            return render(request,'property-grid.html',{'data':result})
        else:
            return HttpResponse(" <h1> No Result Found</h1> ")
    else:
        return HttpResponse(" <h1> Denial </h1>")


def searchbyprice(request):
    if request.method=="POST":
        type_ = request.POST.get('price')
        print(type_)
        result=property.objects.filter(price=type_)
        if result:
            return render(request,'property-grid.html',{'data':result})
        else:
            return HttpResponse(" <h1> No Result Found</h1> ")
    else:
        return HttpResponse("<h1> Denial </h1>")