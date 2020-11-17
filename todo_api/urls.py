from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = DefaultRouter()
router.register('user', views.UserProfileViewSet)
router.register('todo', views.TodoStuffViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token)
]
