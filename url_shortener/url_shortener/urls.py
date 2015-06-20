from django.conf.urls import include, url
from django.contrib import admin
# from django.shortcuts import redirect

from shorturls.views import LinkCreate, LinkShow, RedirectToLongURL, LinkList

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^$', LinkCreate.as_view(), name='home'),
    url(r'^link/(?P<pk>\d+)$', LinkShow.as_view(), name='link_show'),
    url(r'^r/(?P<short_url>\w+)$', RedirectToLongURL.as_view(), name='redirect_short_url'),
    url(r'^users/(\w+/)?$', LinkList.as_view(), name='link_list'),
    # url(r'^$', lambda r: redirect('/admin'), name='home'),
]
