from django.conf.urls import patterns, include, url

urlpatters = patterns('contact.views',
	url(r'^index/$', 'contact_index', name='contact_index'),
	)