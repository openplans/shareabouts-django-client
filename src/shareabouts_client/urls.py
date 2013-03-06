from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = staticfiles_urlpatterns() + patterns('',
    # Examples:
    # url(r'^$', 'shareabouts_client.views.home', name='home'),
    # url(r'^shareabouts_client/', include('shareabouts_client.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^api/(.*)$', views.api, name='api_proxy'),
    url(r'^download/(.*).csv$', views.csv_download, name='csv_proxy'),
    url(r'^', views.index, name='index'),
)
