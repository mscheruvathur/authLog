from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_control
# Create your views here.
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def registrasion(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:

        if request.method == 'POST':
            user_name = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            email = request.POST['email']
            
            if password1 == password2 :
                if User.objects.filter(username=user_name).exists():
                    messages.info(request,"Username Taken")
                    return redirect('signup')
                else:
                    user = User.objects.create_user(username=user_name,password=password1,email=email)    
                    user.save()
                    print('user created')
                    return redirect('login')
            else:
                messages.info(request,"Password Does not match")
        else:
            return render(request,'signup.html')
        
        return render(request,'signup.html')

@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def login(request):

    if request.user.is_authenticated:
        return redirect('/')
    else:

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username,password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                messages.info(request,'Invalid Credential')
                return redirect('login')
        else:
            return render(request,'login.html')
        return render(request,'login.html')

@never_cache
@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
@login_required(login_url="login")
def home_page(request):
    
    return render(request,'home.html')

def login_page(request):
    return render(request,'index.html')


@cache_control(max_age=0, no_cache=True, no_store=True, must_revalidate=True)
def logout(request):
    
    auth.logout(request)
    request.session['is_logged'] = True
    return redirect('login')    