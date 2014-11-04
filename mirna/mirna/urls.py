from django.conf.urls import patterns, include, url
from mirna.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'apiSrv.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

	
    url(r'^mirna/$', mirna_view),
    url(r'^mirna/(?P<id>\d+)/$', mirna_detail_view),

)
