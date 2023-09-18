from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

################# User Authentication ###################
def loginView(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home_url')
        else:
            messages.error(request,"Wrong Credentials", extra_tags='login')
            return render(request, 'login.html')
    else:
        return render(request,'login.html')

def registerView(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if fname!='' and lname!='' and username!='' and email!='' and pass1!='' and pass2!='':
            #password 
            if pass1==pass2:
                #user exists
                if User.objects.filter(username=username).exists():
                    messages.error(request,"Username already taken", extra_tags='register')
                    return HttpResponseRedirect(request.path_info)
                #email exists
                if User.objects.filter(email=email).exists():
                    messages.error(request,"Email already taken", extra_tags='register')
                    return HttpResponseRedirect(request.path_info)
                else:
                    user=User.objects.create(username=username, first_name=fname, last_name=lname, email=email, password=pass1)
                    user.save()
                    if user is not None:
                        auth.login(request, user)
                        return redirect('home_url')
            else:
                messages.error(request,"Your passwords didn't match",  extra_tags='register')
                return HttpResponseRedirect(request.path_info)
        else:
            messages.error(request,'Please fill out all fields',  extra_tags='register')
            return HttpResponseRedirect(request.path_info)
    else:
        return render(request,'login.html')

def logoutView(request):
    auth.logout(request)
    return redirect('home_url')
