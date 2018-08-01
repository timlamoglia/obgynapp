from django.urls import path, include

from . import views

app_name = 'patients'
urlpatterns = [
	path('', views.index, name='index'),
	path('<int:patient_id>/', views.show, name='show'),
	path('new/', views.new, name='new'),
	path('<int:patient_id>/edit/', views.edit, name='edit'),
	path('<int:patient_id>/delete/', views.delete, name='delete'),
]