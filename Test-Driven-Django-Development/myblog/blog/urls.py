from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<years>\d{4})/(?P<months>\d{1,2})/(?P<days>\d{1,2})/(?P<pk>\d+)-(?P<slug>[-\w]*)/$', views.EntryDetail.as_view(), name='entry_detail'),
]
