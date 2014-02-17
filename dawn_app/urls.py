from django.conf.urls import *

urlpatterns = patterns(('dawn_app.views'),
    url(r'^bloglist/$', 'blog_list', name= 'bloglist'),
    url(r'^blog/(?p<id>\d+)/$', 'blog_show', name='detailblog'),
)
