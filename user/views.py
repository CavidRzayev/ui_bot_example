from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import User
from django.core.mail import send_mail

def logins(request):
    if request.method == 'POST':
        
        user = authenticate(email=request.POST.get("email"), password=request.POST.get("password"))
        if user is not None:
            if user.is_verify == True:
                login(request,user)
                return redirect("index")
            else:
                messages.info(request, "Please verify your email")
        else:
            messages.warning(request, "Email or password incorrect!")
    return render(request,"auth/login.html")

def register(request):
    if request.method == 'POST':
        user = request.POST.get("email")
        password = request.POST.get("password")
        current_password = request.POST.get("current_password")
        if user:
            check_user = User.objects.filter(email=user)
            if len(check_user) > 0:
                messages.warning(request, "User is exist!")
            else:
                if password == current_password:
                    check_email = user.split("@")
                    print(check_email)
                    if check_email[1] == "abb-bank.az":
                        user = User.objects.create(email=user,password=password,is_verify=True)
                        user.set_password(password)
                        user.save()
                        users = authenticate(email=user, password=password)
                        login(request,users)
                        #text = f"http://ai.abb-bank.az:8888/auth/verify?email={user.email}"
                        #messages.success(request, "User successfully created please verify your email")
                        #send_emil = send_mail('Verify your email', f'Please click the link : {text} ','abbaibot@yandex.ru',[f'{user.email}'],fail_silently=False)
                        #print(send_emil)
                        return redirect("index")
                    else:
                        messages.info(request, "Only Abb User")

                else:
                    messages.warning(request, "Password or current password incorrect!")


    return render(request,"auth/register.html")


def logouts(request):
    logout(request)
    return redirect("login")


def check_verify(request):
    email = request.GET.get("email")
    get_user = User.objects.get(email=email)
    get_user.is_verify = True
    get_user.save()
    return redirect("login")
