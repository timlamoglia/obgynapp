from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views


app_name = 'dashboard'
urlpatterns = [
	#path('', views.index, name='index')
	path('', auth_views.login, {'template_name': 'login.html'}, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]