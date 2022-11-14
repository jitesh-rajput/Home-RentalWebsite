from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from Property.models import property,property_image,Card
from Rent.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from .models import User
# Create your views here.

def home_review(request,id):
    property_info=property.objects.get(id=id)
    print(property_info.location)
    property_img=property_image.objects.filter(property_id=id)
    print(property_img)
    data={
        'property_img':property_img,
        'property_info':property_info,
    }
    return render(request,'property-single.html',{'data':data})

def seeproperty(request):
    data = property.objects.all()
    print(data)
    print(type(data[0].id))
    return render(request,'property-grid.html',{'data':data})

def book(request,id):
    user = User.objects.filter(username=request.user)
    if user:
        info = User.objects.get(username=request.user)
        email = info.email
        subject = ' Murugan rentals tak'
        message = " Contact details of Agent is :- Email :- ,Phone No- 55544,Mobile-Number:-9403683589"
        recepient = str(email)
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
        return render(request, "Book.html")
    else:
        return HttpResponse(" <h1> User is Not Log In </h1>")


def home(request):
    return HttpResponseRedirect("/index.html")

def add_fev(request,id):
    user=User.objects.filter(username=request.user)
    if user:
        pos=property.objects.get(id=id)
        card=Card(username=user[0],property_id=pos,is_fav=True)
        card.save()
        return render(request,"index.html")
    else:
        return HttpResponse(" <h1> User is Not Log In </h1>")

def searchbytype(request):
    if request.method=="POST":
        type_ = request.POST.get('type')
        print(type_)
        return HttpResponse(" dfasdf")