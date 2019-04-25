from django.db import models

# Create your models here.

class MovieDetails(models.Model):
	name = models.CharField(max_length=64,unique=True, blank = False)
	genre = models.CharField(max_length=32,blank = False)
	status = models.CharField(max_length=32,blank = False)
	total_seats = models.PositiveSmallIntegerField(blank = False)
	booked_seats =  models.PositiveSmallIntegerField(default=0)

	@property
	def available_seats(self):
		return self.total_seats - self.booked_seats

	@property
	def ticket_available(self):
		status = False
		if self.available_seats > 0:
			status = True
		return status

	def __str__(self):
		return self.name

	