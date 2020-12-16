from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


# Create your views here.
def login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            if request.POST['username'] and request.POST['password']:
                username = request.POST["username"]
                password = request.POST["password"]

                user = auth.authenticate(username =username,password =password)

                if user is not None:
                    auth.login(request,user)
                    if request.POST['next'] != '':
                        return redirect(request.POST.get('next'))
                    else:
                        return redirect('/')
                else:
                    messages.info(request, 'User does not exist')
                return redirect('login')
            else:
                return render(request, 'login.html', {'error': "Empty Fields"})
        else:
            return render(request, 'login.html')
    else:
        return redirect('/')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password1']
        c_password = request.POST['password2']
        email = request.POST['email']

        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save();
                print('New User created')
                return redirect('login')

        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
        return redirect('/')

    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

