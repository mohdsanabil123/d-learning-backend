from django.urls import path, include
from rest_framework import routers
from .views import UserViewSet, NewsViewSet, user_account, user_profile, NotesViewSet, get_notes, ContactViewSet
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'news', NewsViewSet)
router.register(r'notes', NotesViewSet)
router.register(r'contact', ContactViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('account/<int:user_id>/', user_account),
    path('account/', user_account),
    path('profile/', user_profile),
    path('token-auth/', views.obtain_auth_token),
    path('Notes/<str:subject>/<int:s_class>/', get_notes),
]
