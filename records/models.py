from django.db import models

# Create your models here.

from patients.models import Patient

class Record(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	visit_date = models.DateField()
	bp = models.CharField(max_length=20)
	fh = models.CharField(max_length=20)
	fht = models.CharField(max_length=20)
	lmp = models.DateField()
	edc = models.DateField()	# lmp + 280 days
	aog = models.FloatField() # edc - current_date
	diagnosis = models.CharField(max_length=1000)
	medication = models.CharField(max_length=1000)
	return_date = models.DateField()

	def __str__(self):
		return self.visit_date.strftime('%A %d %B %Y') + ' - ' + self.patient.name

	def get_absolute_url(self):
		return reverse('patient_edit', kwargs={'pk': self.pk})