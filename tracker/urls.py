"""TODO"""

from django.conf.urls import url, include
from rest_framework import routers

from tracker import views
from .views import (
    TicketsListView,
    TicketCreateView,
    TicketDetailView,

    ImpactChoicesView,
    PriorityChoicesView,
    TimeSensitivenessChoicesView,
    ReproducibilityChoicesView,
    AnomalyTypeChoicesView,
)

urlpatterns = [  # pylint: disable=invalid-name
    url(r"^tracker/$",
        TicketsListView.as_view(),
        name="list"),
    url(r"^tracker/create/(?P<type>[-_\w]+)/$",
        TicketCreateView.as_view(),
        name="create"),
    url(r"^tracker/export/$",
        TicketsListView.as_view(),
        name="export"),
    url(r"^tracker/(?P<pk>[-_\w]+)/$",
        TicketDetailView.as_view(),
        name="detail"),
    url(r"^tracker(?P<pk>[-_\w]+)/update/$",
        TicketsListView.as_view(),
        name="update"),
    url(r"^tracker/(?P<pk>[-_\w]+)/validate/$",
        TicketsListView.as_view(),
        name="validate"),

    url(r"^tracker/choices/impact/$",
        ImpactChoicesView.as_view(),
        name="choices_impact"),
    url(r"^tracker/choices/priority/$",
        PriorityChoicesView.as_view(),
        name="choices_priority"),
    url(r"^tracker/choices/priority/$",
        TimeSensitivenessChoicesView.as_view(),
        name="choices_time_sensitiveness"),
    url(r"^tracker/choices/reproducibility/$",
        ReproducibilityChoicesView.as_view(),
        name="choices_reproducibility"),
    url(r"^tracker/choices/anomaly_type/$",
        AnomalyTypeChoicesView.as_view(),
        name="choices_anomaly_type"),
]
