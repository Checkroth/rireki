from django.db import models

# Create your models here.
class Example(models.Model):
	# Find a way to allow actual formatted bullet points within a django Text Field!
	title = models.CharField(max_length=255)
	description = models.TextField()
	link = models.URLField(null=True, blank=True)
	source_link = models.URLField(null=True, blank=True)
	published = models.BooleanField(default=False)

	# Need to set up asset information for this field
	# image = models.ImageFIeld(upload_to='examples', max_length=255)
