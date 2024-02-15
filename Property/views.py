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
        subject = ' Home Rental Website'
        message = "For More detail Information Contact :- 8237238080"
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

def search(request):
    if request.method=="POST":
        type_ = request.POST.get('type')
        city_ = request.POST.get('city')
        price_ = request.POST.get('price')
        print(type_,city_,price_)     
        if(price_!="All"):
            price_=int(price_)
        if(type_!="All" and city_=="All" and price_=="All"):
            result=property.objects.filter(type=str(type_))
        elif(type_!="All" and city_!="All" and price_=="All"):
            result=property.objects.filter(type=str(type_),city=str(city_))
        elif(type_!="All" and city_!="All" and price_!="All"):
            result=property.objects.filter(type=str(type_),city=str(city_),price__gt=price_)
        elif(type_=="All" and city_!="All" and price_!="All"):
            result=property.objects.filter(city=str(city_),price__gt=price_)
        elif(type_=="All" and city_=="All" and price_!="All"):
            result=property.objects.filter(price__gt=price_)
        elif(type_=="All" and city_!="All" and price_!="All"):
            result=property.objects.filter(city=str(city_),price__gt=price_)
        elif(type_=="All" and city_!="All" and price_=="All"):
            result=property.objects.filter(city=str(city_))
        else:
            result=property.objects.filter()
        print("result ",result)
        if result:
            return render(request,'property-grid.html',{'data':result})
        else:
            return HttpResponse(" <h1> No Result Found</h1> ")
    else:
        return HttpResponse(" <h1> Denial </h1>")
        
def profile(request):
    user=User.objects.get(username=request.user)
    return render(request,'profile.html',{'user':user})

def logout(request):
    auth.logout(request)
    return render(request,'index.html')