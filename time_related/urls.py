from django.conf.urls import url

from time_related.views import ManageSchedule
from .import views

urlpatterns = [
    url(r'^$', views.schedule, name='schedule'),
    url(r'^manage_schedule/$', ManageSchedule.as_view(), name="manage_schedule"),
    # url(r'^post/$', ManageSchedule.as_view()),
    # url(r'^delete_object/$', views.delete_object, name="delete_object"),
]