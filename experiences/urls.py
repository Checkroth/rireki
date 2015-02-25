import experiences
from django.conf.urls import patterns, include, url

urlpatterns = patterns('experiences.views',
	url(r'^experience/$', 'experience_index', name='experience_index'),
	)