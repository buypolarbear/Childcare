"""Child_care URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from app.views import (IndexView, ChildCreateView, ChildStatusTimeCreateView, ChildStatusUpdateView,
                       BlahView, ChildListView, ChildCheckIn_LogListView, ChildUpdateView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^blah/$', BlahView.as_view(), name='blah_view'),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^child/create/$', ChildCreateView.as_view(), name='child_create_view'),
    url(r'^child/(?P<pk>\d+)/update/$', ChildUpdateView.as_view(), name='child_update_view'),
    url(r'child_status/(?P<pk>\d+)/create/$', ChildStatusTimeCreateView.as_view(), name='child_status_time_create_view'),
    url(r'^child_status/(?P<pk>\d+)/update/$', ChildStatusUpdateView.as_view(), name='child_status_update_view'),
    url(r'^child_list/$', ChildListView.as_view(), name="child_list_view"),
    url(r'^checkin_log/(?P<pk>\d+)/$', ChildCheckIn_LogListView.as_view(), name="child_checkin_log_list_view")
]
