from django.shortcuts import render


def landing_view(request):
	pass


def test_view(request):
	return render(request, 'views/index.html')
