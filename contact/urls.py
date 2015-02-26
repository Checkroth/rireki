from django.conf.urls import patterns, include, url

urlpatterns = patterns('contact.views',
	url(r'^contact/$', 'contact_index', name='contact_index'),
	)