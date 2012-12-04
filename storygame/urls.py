from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'storygame.views.home', name='home'),
    # url(r'^storygame/', include('storygame.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^stories/(?P<slug_story>[\w.\-]+)/', include(
    	'storygame.stories.urls',
    	namespace='stories'
    	) )
)