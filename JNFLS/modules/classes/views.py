from django.shortcuts import render


# Create your views here.
def school_class_view(request):
	return render(request, 'views/class.html')
