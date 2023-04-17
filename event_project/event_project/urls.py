"""
URL configuration for event_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from accounts.views import CreateNewUser,ListUser,LoginUser,LogoutUser,NewPassword,Profile
from event_app.views import NewEvent, SearchEvents, JoinEventAPIView,ReportEvents,ListEvents
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'CreateEvents', NewEvent, basename='CreateEvents')

# router.register(r'searchevent', SearchEvents, basename='searchevent')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_user/',CreateNewUser.as_view()),
    path('list_user/',ListUser.as_view()),
    path('login_user',LoginUser.as_view()),
    path('logout_user',LogoutUser.as_view()),
    path('search',SearchEvents.as_view()),
    path('Join/<int:pk>',JoinEventAPIView.as_view()),
    path('listEvents',ListEvents.as_view),
    path('change_pass',NewPassword.as_view()),
    path('password_reset', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('view_profile/',Profile.as_view()),
    path('report',ReportEvents.as_view()),
    path('', include(router.urls))

]

# urlpatterns += router.urls
