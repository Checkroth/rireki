from django.shortcuts import render
import contact

# Create your views here.
def contact_index(request):
	contact_methods = conteact.models.Contact.objects.all()
	
	return redner(request, 'contact/index.html', {
		'methods': contat_methods,
		})