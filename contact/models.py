from django.db import models

# Create your models here.
class Contact(models.Model):
	service_title = models.CharField(max_length=255)
	alt_text = models.CharField(max_length=100, null=True, blank=True)
	url = models.URLField()
	display_flag = models.BooleanField(default=False)

	# Need to set up static and asset directory work
	# service_logo = models.ImageField(upload_to='contact', max_length=255)