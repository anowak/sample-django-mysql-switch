from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('django_mysql.views',
  url(r'^$',   'greet')
)
