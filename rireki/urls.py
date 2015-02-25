from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
	(r'', include('contact.urls')),
	(r'', include('examples.urls')),
	(r'', include('experiences.urls')),
	(r'', include('static_pages.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )