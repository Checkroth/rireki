from django.conf.urls import patterns, include, url

urlpatterns = patterns('static_pages.views',
	url(r'^$', 'home', name='home'),
	)