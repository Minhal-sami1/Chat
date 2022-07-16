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
# Create your views here.

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")

@login_required(login_url="login")
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")

@login_required(login_url="login")
def index(request):
    return render(request,"index.html")


@login_required(login_url="login")
def get_unique_id(request):
    unique_id = User.objects.get(username=request.user)
    return render(request,"getid.html",{
        "unique_id":unique_id.seperation
    })
global curr 
curr = 0
@login_required(login_url="login")
def connect(request):
    if request.method == "POST":
        connect_id = request.POST['connectid']
        try:
            user_data = User.objects.get(seperation=connect_id)
            if request.user == user_data:
                return HttpResponseRedirect(reverse("connect"))
            else:
                return redirect(reverse("message", args=(f"{connect_id}",)))
        except User.DoesNotExist:
            return HttpResponseRedirect(reverse("connect"))
    else:    
        return render(request,"inputid.html")

def get_messages(request, userf, usert):
    try:
        connect_id = User.objects.get(seperation=usert)
        current_user = User.objects.get(username=request.user)
        f1 = Q(user_from = current_user)
        f3 = Q(user_from = connect_id)
        #messages_old = Message.objects.filter( f1 | f3).order_by("time") 
        try:
            messages_new = Message.objects.filter(f1 | f3).order_by("time")
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

@login_required(login_url="login")
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
        return render(request, "messages.html",{
        "userid":user_id,
        "uston": connect_id,
        "curr":current_user,
        #"ms": messages_old
        })
    except User.DoesNotExist:
        print("not found")
        return HttpResponseRedirect(reverse("connect"))

