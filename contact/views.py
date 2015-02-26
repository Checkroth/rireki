from django.shortcuts import render
import contact

# Create your views here.
def contact_index(request):
	contact_methods = contact.models.Contact.objects.all()
	
	return render(request, 'contact/index.html', {
		'methods': contact_methods,
		})