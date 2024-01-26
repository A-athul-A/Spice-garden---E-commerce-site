from django.shortcuts import render,redirect
from django.contrib import messages, auth
from django.contrib.auth import login as authlogin,logout as authlogout, authenticate
from django.contrib.auth.models import User
from . models import product_tbl
from cart.models import Direct_buy
from django.db.models import Q

# Create your views here.


def index(request):
    obj = product_tbl.objects.all()
    if obj:
        return render(request,"index.html",{"data":obj})
    return render(request,'index.html')


def signup(request):
    if request.POST:
        username = request.POST["rmail"]
        password = request.POST["rpass"]
        first_name = request.POST["rname"]
        try:
            user = User.objects.create_user(username=username,password=password,first_name=first_name)
            return redirect("/")
        except Exception as e:
            error = str(e)
    return render(request,"login.html")

def login(request):
    if request.POST:
        username = request.POST["umail"]
        password = request.POST["upass"]
        user = authenticate(username = username, password = password)
        if user:
            authlogin(request,user)
            return redirect("/",{"user":user})

        else:
            msg = "Invalid username or password"
            return redirect("/login",{"msg":msg})

    return render(request,"login.html")

   
def logout(request):
    authlogout(request)
    return redirect('/')


def view_product(request):
    idn  = request.GET['idn']
    obj = product_tbl.objects.filter(id=idn)
    obj2 = Direct_buy.objects.all()
    obj2.delete()
    return render(request,"product_details.html",{"data":obj})



def search(request):
    query = None

    if 'keyword' in request.GET:
        query = request.GET.get('keyword')
        products = product_tbl.objects.all().filter(Q(product_name__contains=query) | Q(product_price__contains=query))
        return render(request,'search-result.html',{'query':query,'data':products})
 

def about(request):
    return render(request,'about.html')