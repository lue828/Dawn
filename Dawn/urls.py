from django.conf.urls import patterns, include, url

from django.conf import settings
#from django.contrib import admin
#admin.autodiscover()

import xadmin
xadmin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Dawn.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'xadmin/', include(xadmin.site.urls)),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^comments/', include('django.contrib.comments.urls')),
)

urlpatterns += patterns((''),
    (r'^dawn_app/', include('dawn_app.urls')),
)

urlpatterns += patterns((''),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}
    ),
)

urlpatterns += patterns((''),
    url(r"^media/(?P<path>.*)$", "django.views.static.serve",
            {"document_root": settings.MEDIA_ROOT,}),
)