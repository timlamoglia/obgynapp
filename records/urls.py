from django.urls import path

from . import views

app_name = 'records'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:record_id>/', views.show, name='show'),
	path('new/', views.new, name='new'),
	path('<int:record_id>/edit/', views.edit, name='edit'),
	path('<int:record_id>/delete/', views.delete, name='delete')
]