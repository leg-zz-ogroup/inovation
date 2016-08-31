from django.conf.urls import patterns, include, url
from Apps.BaseData import CounterParty
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
    url(r'^$', CounterParty.CounterParty.actual_counterparty_list_maker, name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       # url(r'^admin/', include(admin.site.urls)),
                       )
