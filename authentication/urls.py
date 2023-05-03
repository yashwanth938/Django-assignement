from django.urls import path
from authentication.views import UserCreateAPIView
from artists.views import WorkList, ArtistList

urlpatterns = [
    path('api/works/', WorkList.as_view(), name='work-list'),
    path('api/artists/', ArtistList.as_view(), name='artist-list'),
    path('api/users/create/', UserCreateAPIView.as_view(), name='user-create'),
]
