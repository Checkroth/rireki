from django.db import models

# Create your models here.
class Experience(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	example_link = models.URLField()
	company_link = models.URLField()

	# Need assets set up for this field
	# image = models.ImageField(upload_to='experience', max_length=255)