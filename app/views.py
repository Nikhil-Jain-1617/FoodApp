from .models import *
from app.forms import SignUpForm
from django.http.response import HttpResponse, HttpResponseRedirect
from app.models import Menu, Restaurant, User
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required

# Create your views here.
class About(View):

    def get(self, request):
        return render(request, 'about.html')


class Offer(View):

    def get(self, request):
        return render(request, 'offer.html')


@login_required
def index(request):
    restaurant = Restaurant.objects.all()
    data = {
        "restaurant":restaurant
    }
    return render(request,'index.html',data)
   
@login_required
def menu(request):
    res_Id = request.GET.get("id")
    menu = Menu.objects.filter(restaurant_name=res_Id)
    context = {
        "menu":menu
    }
    return render(request,'menu.html',context)

def signup_view(request):
    form = SignUpForm()
    if request.method == "POST":

        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request,"signup.html",{'form':form})

def logout_view(request):
    return render(request,"logout.html")

class Order(View):
    def get(self,request,pk=None):
        item = Menu.objects.filter(id=pk)
        data = {
            "item":item
        }
        return render(request,'order.html',data)

    def post(self,request,pk=None):
        postdata= request.POST
        username= postdata.get('username')
        contact= postdata.get('contact')
        email= postdata.get('email')
        address= postdata.get('address')
        restaurant= postdata.get('restaurant_name')
        items= postdata.get('items_name')

        print(username, contact, email, address, restaurant, items,)
        user = User(user_name = username,
                        user_contact= contact,
                        user_email= email, 
                        user_address= address, 
                        restaurant_name= restaurant,
                        item_name= items, )

        user.save()
        message = "Thankyou for ordering, please wait for sometime."
        data = {
            "message" : message
        }

        return render(request,'order.html',data)