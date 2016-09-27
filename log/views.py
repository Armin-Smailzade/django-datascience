#!python
#log/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as authLogin

# from django.contrib.auth.forms import UserCreationForm

from log.forms import UserCreateForm, LoginForm

# Create your views here.

# this login required decorator is to not allow to any  
# view without authenticating
@login_required(login_url="log/login/")
def home(request):
	return render(request,"log/home.html")

@login_required(login_url="log/login/")
def index(request):
	return render(request, "log/index.html")

# def login(request):

# 	form = LoginForm()

# 	if request.method == 'POST':
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		user = authenticate(username=username, password=password)
# 		if user is not None:
# 			authLogin(request, user)


# 			return render(request, 'home.html')

# 	return render(request, 'login.html', {'form': form})

# def login(request):

# 	form = LoginForm()

# 	if request.method == 'POST':
# 		loginForm = LoginForm(data=request.POST)
		
# 		if loginForm.is_valid():
			
# 			return render(request, 'home.html')

# 	return render(request, 'login.html', {'form': form})


def register(request):

	form = UserCreateForm()

	if request.method == 'POST':
		formRequest = UserCreateForm(request.POST)
		if formRequest.is_valid():
			formRequest.save()
			return render(request, 'log/home.html')
		else:
			return render(request, 'log/register.html', {'form':formRequest})

	return render(request, 'log/register.html', {'form' : form})