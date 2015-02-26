def site_title(request):
	from django.contrib.sites.models import Site
	try:
		site_title = Site.objects.get_current().personalinfo.site_name
	except:
		site_title = 'My Rireki Page'
	return {
		'site_title': site_title,
	}
