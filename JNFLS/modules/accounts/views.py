from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login

from .forms import LoginForm


def home_view(request):
	if request.user.is_anonymous():
		return redirect('login')
	elif request.user.is_authenticated():
		return render(request, 'views/index.html', {'user': request.user})


def login_view(request):
	if request.method == 'GET':
		return render(request, 'views/login.html')
	elif request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				return render(request, 'views/login.html', {'msg': '用户名或密码错误'}, status=400)
		else:
			return render(request, 'views/login.html', {'msg': '用户名或密码错误'}, status=400)


def register_view(request):
	if request.method == 'GET':
		return render(request, 'views/register.html')
	elif request.method == 'POST':
		pass


def logout_view(request):
	logout(request)
	return redirect('login')
