from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import UserForm

def home(request):
    return render(request,'home.html')



def loging(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return render(request,'landing.html')
        else:
            return render(request,'register.html')

    return render(request,'login.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error_message': 'Username already taken'})

        if password != confirm_password:
            return render(request, 'register.html', {'error_message': 'Passwords do not match'})

        myuser = User.objects.create_user(username, email, password)
        myuser.save()

        return redirect('login')

    return render(request,'register.html')

def back(request):
    return render(request,'back.html')


from django.shortcuts import render, redirect
from django.views import View
from .forms import UserForm

class UserFormView(View):
    template_name = 'back.html'

    def get(self, request):
        form = UserForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('back.html')
        return render(request, self.template_name, {'form': form})
