from django.shortcuts import render, redirect
from django.contrib.auth import authenticate


def landing_view(request):
	pass


def test_view(request):
	return render(request, 'views/index.html')


def login_view(request):
	return render(request, 'views/login.html')


def login_action(request):
	user = authenticate(username='john', password='secret')
	if user is not None:
		return redirect('home')
	else:
		return redirect('login', {'msg': '用户名或密码错误'})

