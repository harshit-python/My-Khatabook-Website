from django.shortcuts import render, redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Transaction

def home(request):
    return render(request, "home.html")

def addnewtrans(request):
    if request.method=="POST":
        trans_from = request.POST['trans_from']
        trans_to = request.POST['trans_to']
        amount = request.POST['amount']
        date = request.POST['date']

        transaction = Transaction.objects.create(trans_from=trans_from, trans_to=trans_to, amount=amount, date=date)
        transaction.save();
        print("transaction added")
        return redirect("addnewtrans")
    
    else:
        return render(request, "addnewtrans.html")

def transactions(request):
    transactions = Transaction.objects.all()
    return render(request, "transactions.html", {"transactions": transactions})

def logout(request):
    return render(request, "login.html")

def login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            return redirect("login")
    else:
        return render(request, "login.html")

def register(request):
    if request.method=="POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        user = User.objects.create_user(username=username, first_name=firstname, last_name=lastname, email=email, password=password1)
        user.save();
        print("user created")
        return redirect("login")

    else:    
        return render(request, "register.html")