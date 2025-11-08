from django.shortcuts import render
from .models import Contact,Signup

# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    if request.method=="POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            remarks=request.POST['remarks'],

        )
        msg="Contact Saved Successfully"
        contacts=Contact.objects.all().order_by("-id")[:3]
        return render(request,'contact.html',{'msg':msg,'contacts':contacts})
    else:
        contacts=Contact.objects.all().order_by("-id")[:3]
        return render(request,'contact.html',{'contacts':contacts})
    

def signup(request):
    if request.method=="POST":
         try:
             Signup.objects.get(email=request.POST['email'])
             msg="Email Already Registered"
             return render(request,'signup.html',{'msg':msg})
         except:
             if request.POST['password']==request.POST['cpassword']:
                 Signup.objects.create(
                     fname=request.POST['fname'],
                     lname=request.POST['lname'],
                     email=request.POST['email'],
                     mobile=request.POST['mobile'],
                     address=request.POST['address'],
                     password=request.POST['password'],
                 )
                 msg="User Signup Successful"
                 return render(request,'signup.html',{'msg':msg})
             else:
                 msg="Pass & Cpass Doesnt Match"
                 return render(request,'signup.html',{'msg':msg})
    else:
        return render(request,'signup.html')



def login(request):
    return render(request,'login.html')