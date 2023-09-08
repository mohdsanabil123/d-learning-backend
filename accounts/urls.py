from django.urls import path, include
from accounts import views
from rest_framework import routers
from .views import UserViewSet
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('token-auth/', views.obtain_auth_token),
]
