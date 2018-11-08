"""Components URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

from tracker import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'impact', views.ImpactViewSet)
router.register(r'priority', views.PriorityViewSet)
router.register(r'timesensitiveness', views.TimeSensitivenessViewSet)
router.register(r'application', views.ApplicationViewSet)
router.register(r'version', views.VersionViewSet)
router.register(r'module', views.ModuleViewSet)
router.register(r'status', views.StatusViewSet)
router.register(r'sprint', views.SprintViewSet)
router.register(r'roadmap', views.RoadmapViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'tickets', views.TicketViewSet)

app_name = "tracker"

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^schedule/', include('time_related.urls')),
    url(r'^index/', include('tracker.urls')),
    url(r'^api-token-auth/', include('rest_framework.urls')),
    url(r'^auth-jwt/', obtain_jwt_token),
    url(r'^auth-jwt-refresh/', refresh_jwt_token),
    url(r'^auth-jwt-verify/', verify_jwt_token),
]
