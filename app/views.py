import json
from django.shortcuts import redirect, render
from django.db import IntegrityError
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .encrypt import decrypt, encrypt
from django.db.models import Q
from django.views import View

class RegisterView(View):
    def get(self, req):
        return render(req, 'account/register.html')

    def post(self, req):
        username = req.POST["username"]
        email = req.POST["email"]
        # Ensure password matches confirmation
        password = req.POST["password"]
        confirmation = req.POST["confirmation"]
        if password != confirmation:
            return render(req, "account/register.html", {
                "message": "Passwords must match."
            })
        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
            login(req, user)
            return HttpResponseRedirect(reverse("index"))
        except IntegrityError:
            return render(req, "account/register.html", {"message": "Username already taken."})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


class LoginView(View):
    def get(self, req):
        return render(req, "account/login.html")

    def post(self, req):
        username = req.POST["username"]
        password = req.POST["password"]
        user = authenticate(req, username=username, password=password)
        if user is not None:
            login(req, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(req, "account/login.html", {"message": "Invalid username and/or password."})

def index(request):
    return render(request,"app/index.html")


def get_unique_id(request):
    unique_id = User.objects.get(username=request.user)
    return render(request,"app/getid.html",{
        "unique_id":unique_id.seperation
    })


global curr 
curr = 0
def connect(request):
    if request.method == "POST":
        connect_id = request.POST['connectid']
        try:
            user_data = User.objects.get(seperation=connect_id)
            if request.user == user_data:
                return HttpResponseRedirect(reverse("connect"))
            else:
                curr = User.objects.get(username=request.user)
                con=Contacted_people(FROM=curr, TO=user_data)
                con.save()
                return redirect(reverse("message", args=(f"{connect_id}",)))
        except User.DoesNotExist:
            return HttpResponseRedirect(reverse("connect"))
    else:    
        return render(request,"app/inputid.html")

def get_messages(request, userf, usert):
    try:
        connect_id = User.objects.get(seperation=usert)
        current_user = User.objects.get(username=request.user)
        f1 = Q(user_from = current_user)
        f3 = Q(user_to = connect_id)
        f2 = Q(user_to = current_user)
        f4 = Q(user_from = connect_id)
        #messages_old = Message.objects.filter( f1 | f3).order_by("time") 
        try:
            messages_new = Message.objects.filter(f1 & f3 | f2 & f4).order_by("time")
        except Message.DoesNotExist:
            messages_new = []
        obj_json = {}
 
        if messages_new == []:
            return JsonResponse({"ENDED":"ENDED"})       
     
        for ms in messages_new:
            text = decrypt(ms.text)
            user_from = ms.user_from.seperation
            user_to = ms.user_to.seperation
            obj_json[ms.id] = [text, user_from, user_to]
        
        return JsonResponse(obj_json)       
    except User.DoesNotExist:
        print("not found")
        return HttpResponseRedirect(reverse("connect"))

def messages(request, user_id):
    if request.method == "POST":
        connect_id = User.objects.get(seperation=user_id)
        message = json.loads(request.body)
        form = Message(text=encrypt(message), user_from = request.user, user_to=connect_id)
        form.save()
        return JsonResponse({"message":"Success"})
        pass
    try:
        connect_id = User.objects.get(seperation=user_id)
        current_user = User.objects.get(username=request.user)
        #f1 = Q(user_from = current_user)
        #f3 = Q(user_from = connect_id)
        #messages_old = Message.objects.filter( f1 | f3).order_by("time")
        #global curr
        #for ms in messages_old:
            #curr = ms.id
        #print(curr)
        return render(request, "app/messages.html",{
        "userid":user_id,
        "uston": connect_id,
        "curr":current_user,
        #"ms": messages_old
        })
    except User.DoesNotExist:
        print("not found")
        return HttpResponseRedirect(reverse("connect"))

def Already_contacted(request):
    try:
        requested_USER = User.objects.get(username = request.user)
        people_contacted = Contacted_people.objects.filter(FROM = requested_USER)
        otherone = Contacted_people.objects.filter(TO = requested_USER)
        return render(request, "app/Contacted.html", {"contacted": people_contacted, "otherone": otherone})
    except User.DoesNotExist:
        return HttpResponseRedirect(reverse("index"))