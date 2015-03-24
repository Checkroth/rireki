from django.shortcuts import render
import static_pages

# Create your views here.
def home(request):
	try:
		main_description = static_pages.models.PersonalInfo.objects.get(id=0).main_description
	except static_pages.models.PersonalInfo.DoesNotExist:
		main_description = 'Please create a main site description in the CMS, located at [your-site]/admin"<br /><br />\
			The default login is: <br />\
			Username: admin<br />\
			Password: password'

	return render(request, 'static_pages/index.html', {
		'main_description': main_description,
		})