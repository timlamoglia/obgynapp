from django.forms import ModelForm
from patients.models import Patient

class PatientForm(ModelForm):
	class Meta:
		model = Patient
		fields = '__all__'
