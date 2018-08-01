from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.template import loader
from django import forms

from patients.models import Patient

# Create your views here.

class DateInput(forms.DateInput):
	input_type = 'date'

class PatientForm(ModelForm):
	class Meta:
		model = Patient
		fields = '__all__'
		widgets = {
			'birth_date': DateInput(),
		}

def index(request):
	patient_list = Patient.objects.all()
	context = {
		'patient_list': patient_list
	}
	return render(request, 'patients/index.html', context)

def show(request, patient_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	return render(request, 'patients/show.html', {'patient': patient})

def new(request):
	form = PatientForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('patients:index')
	return render(request, 'patients/form.html', {'form': form})

def edit(request, patient_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	form = PatientForm(request.POST or None, instance=patient)
	if form.is_valid():
		form.save()
		return redirect('patients:index')
	return render(request, 'patients/form.html', {'form': form})

def delete(request, patient_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	if request.method=='POST':
		patient.delete()
		return redirect('patients:index')
	return render(request, 'patients/delete.html', {'patient': patient})