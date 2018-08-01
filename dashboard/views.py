from django.shortcuts import render

def index(request):
	context = {
		'welcome': "hi"
	}
	return render(request, 'login.html', context)