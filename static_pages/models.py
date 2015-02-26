from django.db import models
from django.contrib.sites.models import Site

# Create your models here.
class PersonalInfo(models.Model):
	# Method for ensuring that only one instance of this model exists
	# 	Any extra db entries would be meaningless and should not be possible
	site = models.OneToOneField(Site)
	site_name = models.CharField(max_length=255)
	main_description = models.CharField(max_length=255)