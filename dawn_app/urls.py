from django.conf.urls import *


urlpatterns = patterns(('dawn_app.views'),
    url(r'^bloglist/$', 'blog_list', name= 'bloglist'),
    url(r'^blog/(?P<id>\d+)/$', 'blog_show', name='detailblog'),
    url(r'^blog/tag/(?P<id>\d+)/$', 'blog_filter', name='filtrblog'),
    url(r'^blog/add/$', 'blog_add', name='addblog'),
    url(r'^blog/(?P<id>\w+)/update/$', 'blog_update', name='updateblog'),
    url(r'^blog/(?P<id>\w+)/del/$', 'blog_del', name='delblog'),
)
