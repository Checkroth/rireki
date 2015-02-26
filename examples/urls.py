import examples
from django.conf.urls import patterns, include, url

urlpatterns = patterns('examples.views',
	url(r'^examples/$', 'examples_list', name='examples_index'),
	url(r'^examples/(?P<example_id>[0-9]+)/$', 'show_example', name='show_example'),
	)