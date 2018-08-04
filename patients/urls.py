from django.urls import path, include
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'patients'
urlpatterns = [
	path('', login_required(views.PatientListView.as_view()), name='patients'),
	path('<int:patient_id>/', views.show, name='show'),
	path('new/', views.new, name='new'),
	path('<int:patient_id>/edit/', views.edit, name='edit'),
	path('<int:patient_id>/delete/', views.delete, name='delete'),
]