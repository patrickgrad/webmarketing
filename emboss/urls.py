from django.conf.urls import url
from . import views
from emboss.views import New, NewSpecific

urlpatterns = [
	# ex: /emboss/
    url(r'^$', views.dashboard, name='dashboard'),
    # ex: /emboss/s/
    url(r'^s/$', views.splash, name='splash'),
    # ex: /emboss/detail/<media_id>
    url(r'^detail/(?P<media_id>[0-9]+)/$', views.detail, name='detail'),

    # ex: /emboss/new/
    url(r'^new/$', New.as_view(), name='new'),
    # ex: /emboss/new/
    url(r'^new/(?P<media_type>[0-9]+)/$', NewSpecific.as_view(), name='newSpecific'),

    # ex: /emboss/edit/<media_id>
    url(r'^edit/(?P<media_id>[0-9]+)/$', views.edit, name='edit'),

    # ex: /emboss/p/<media_id/<lead_id>
    url(r'^p/(?P<media_id>[0-9]+)/(?P<lead_id>[0-9]+)/$', views.productionWLead, name='productionWLead'),
    # ex: /emboss/p/<media_id>
    url(r'^p/(?P<media_id>[0-9]+)/$', views.productionWOLead, name='productionWOLead'),
]