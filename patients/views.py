from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.template import loader
from django import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.http import HttpResponse
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from patients.models import Patient
from .forms import PatientForm

class PatientListView(ListView):
	model = Patient
	template_name = "patients/patients.html"
	page_template = "patients/patients.html"
	context_object_name = "patient_list"
	paginate_by = 10

	def get_queryset(self):
		query = self.request.GET.get('q')
		if query:
			q_part,q_totals = Q(),Q()
			for part in query.split():
				q_part = q_part & Q(**{'name__icontains':part})
			q_totals = q_totals | q_part
			
			return Patient.objects.filter(q_totals)
		else:
			print(Patient.objects.all())
			return Patient.objects.all().order_by('name');

	def get_context_date(self, **kwargs):
		context = super(PatientListView, self).get_context_data(**kwargs)
		list_patient = Patient.objects.all()
		paginator = Paginator(list_patient, self.paginate_by)

		page = self.request.GET.get('page')

		try:
			patients = paginator.page(page)
		except PageNotAnInteger:
			patients = paginator.page(1)
		except EmptyPage:
			patients = paginator.page(paginator.num_pages)

		context['patient_list'] = patients

@login_required(login_url='/')
def show(request, patient_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	return render(request, 'patients/show.html', {'patient': patient})

@login_required(login_url='/')
def new(request):
	form = PatientForm(request.POST or None)
	if form.is_valid():
		patient = form.save()
		return HttpResponseRedirect(reverse('patients:show', args=(patient.id,)))
	return render(request, 'patients/form.html', {'form': form})

@login_required(login_url='/')
def edit(request, patient_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	form = PatientForm(request.POST or None, instance=patient)
	patient.birth_date = patient.birth_date.strftime('%m/%d/%Y')
	if form.is_valid():
		form.save()
		return HttpResponseRedirect(reverse('patients:show', args=(patient.id,)))
	return render(request, 'patients/form.html', {'form': form, 'patient': patient})

@login_required(login_url='/')
def delete(request, patient_id):
	patient = get_object_or_404(Patient, pk=patient_id)
	if request.method=='POST':
		patient.delete()
		return redirect('patients:patients')
	return render(request, 'patients/delete.html', {'patient': patient})