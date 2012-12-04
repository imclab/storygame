from django.conf.urls import patterns, include, url

urlpatterns = patterns('storygame.stories.views',
    url(r'^$', 'detail', name='detail'),
    url(r'^(?P<activation_key>\w+)/$', 'write', name='write'),
)