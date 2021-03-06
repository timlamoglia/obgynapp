from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.forms import ModelForm
from django.urls import reverse
from django import forms
from django.contrib.auth.decorators import login_required

from .models import Record, Patient

# Create your views here.

# class DateInput(forms.DateInput):
# 	input_type = 'date'

class RecordForm(ModelForm):
	class Meta:
		model = Record
		fields = '__all__'
		# widgets = {
		# 	#'patient': forms.TextInput(attrs={'disabled': True, 'hidden': True}),
		# 	'patient': forms.HiddenInput(),
		# 	'visit_date': DateInput(),
		# 	'lmp': DateInput(),
		# 	'edc': DateInput(),
		# 	'aog': forms.TextInput(),
		# 	'return_date': DateInput()
		# }

@login_required(login_url='/')
def index(request, patient_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	record_list = patient.record_set.all().order_by('visit_date')
	context = {
		'patient': patient,
		'record_list': record_list
	}
	return render(request, 'records/index.html', context)

@login_required(login_url='/')
def show(request, patient_id, record_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	record = get_object_or_404(Record, pk=record_id)
	return render(request, 'records/show.html', {'record': record, 'patient': patient})

@login_required(login_url='/')
def new(request, patient_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	form = RecordForm(request.POST or None, initial={'patient': patient})
	if form.is_valid():
		record = form.save()
		return HttpResponseRedirect(reverse('records:show', args=(patient_id, record.id)))
	return render(request, 'records/form.html', {'form': form, 'patient': patient})

@login_required(login_url='/')
def edit(request, patient_id, record_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	record = get_object_or_404(Record, pk=record_id)
	form = RecordForm(request.POST or None, instance=record)
	record.visit_date = record.visit_date.strftime('%m/%d/%Y')
	record.lmp = record.lmp.strftime('%m/%d/%Y')
	record.edc = record.edc.strftime('%m/%d/%Y')
	record.return_date = record.return_date.strftime('%m/%d/%Y')
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('records:show', args=(patient_id, record.id)))
	return render(request, 'records/form.html', {'form': form, 'patient': patient, 'record': record})

@login_required(login_url='/')
def delete(request, patient_id, record_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	record = get_object_or_404(Record, pk=record_id)
	if request.method=='POST':
		record.delete()
		return HttpResponseRedirect(reverse('records:index', args=(patient_id,)))
	return render(request, 'records/delete.html', {'patient': patient, 'record': record})