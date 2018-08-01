from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Patient(models.Model):
	name = models.CharField(max_length=100)
	birth_date = models.DateField()
	SEX_CHOICES = (
		('MALE', 'Male'), 
		('FEMALE', 'Female')
	)
	sex = models.CharField(max_length=6, choices=SEX_CHOICES)	# male, female
	STATUS_CHOICES = (
		('SINGLE', 'Single'),
		('MARRIED', 'Married'),
		('WIDOWED', 'Widowed'),
		('DIVORCED', 'Divorced'),
		('SEPARATED', 'Separated')
	)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES)	# single, married, widowed, divorced, separated
	address = models.CharField(max_length=200, null=True, blank=True)
	g = models.IntegerField(null=True, blank=True)
	p = models.IntegerField(null=True, blank=True)
	a1 = models.IntegerField(null=True, blank=True)
	a2 = models.IntegerField(null=True, blank=True)
	a3 = models.IntegerField(null=True, blank=True)
	a4 = models.IntegerField(null=True, blank=True)
	phone = models.CharField(max_length=20, null=True, blank=True)
	religion = models.CharField(max_length=50, null=True, blank=True)
	operations_history = models.CharField(max_length=1000, null=True, blank=True)
	allergies_history = models.CharField(max_length=1000, null=True, blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('edit', kwargs={'pk': self.pk})

	def get_age(self):
		today = timezone.now()
		return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))