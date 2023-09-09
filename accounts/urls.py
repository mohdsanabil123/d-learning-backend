from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, NewsViewSet, user_account, user_login
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'news', NewsViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('account/<int:user_id>/', user_account),
    path('account/', user_account),
    path('login/', user_login),
    path('token-auth/', views.obtain_auth_token),
]
