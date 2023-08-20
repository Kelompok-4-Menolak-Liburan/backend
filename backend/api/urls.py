from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import *
from django.conf import settings

urlpatterns = [
    path('auth/', TokenObtainPairView.as_view(),name='api_token_auth'),
    path('auth/register/', RegisterUserView.as_view(),name='api_token_register'),
    path('auth/refresh/', TokenRefreshView.as_view(),name='api_token_refresh'),
    path('auth/logout/', LogoutView.as_view(),name='api_token_logout'),
    path('event/<uuid:id>/',EventRetreiveView.as_view(),name='event_retreive'),
    path('event/update/<uuid:id>/',EventUpdateView.as_view(),name='event_update'),
    path('event/',EventListView.as_view(),name='event_list'),
    path('ownevent/',EventListOwnerView.as_view(),name='event_own_list'),
    path('event/create/',EventCreateView.as_view(),name='event_create'),
]

