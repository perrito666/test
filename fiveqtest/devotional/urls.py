# -*- coding: utf-8 *-*
from django.conf.urls import patterns, url


urlpatterns = patterns('devotional.views',
    url("^(?P<pk>\d+)/$", "detail", name="detail_view"),
    url("^count/(?P<pk>\d+)/$", "wordcount", name="wordcount"),
    url("^$", "detail_form", name="devotional_form"),
    )