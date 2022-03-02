from django.urls import path,include
from watchlist_app.api.views import (StreamPlatformListAV,StreamPlatformDetailsAV,
                                     WatchListAV,WatchListDetailsAV,ReviewDetailListAV,
                                     ReviewDetailsAV,ReviewCreate,ReviewListAV,AddWatchlist)
# from watchlist_app.api.views import StreamPlatformViewset
from rest_framework.routers import DefaultRouter

# router=DefaultRouter()
# router.register('platform',StreamPlatformViewset,basename='streamplatform')


urlpatterns = [
    # path('',include(router.urls)),
    path('platform/',StreamPlatformListAV.as_view(),name='platform-list'),
    path('platform/<int:pk>/',StreamPlatformDetailsAV.as_view(),name='platform-detail'),
    path('platform/<int:pk>/add-movie',AddWatchlist.as_view(),name='add-movies'),
    
    path('list/',WatchListAV.as_view(),name='watchlist-list'),
    path('list/<int:pk>/',WatchListDetailsAV.as_view(),name='watchlist-detail'),
    
    
    path('review/<int:pk>',ReviewDetailsAV.as_view(),name='watchlist-detail'),
    path('review/',ReviewListAV.as_view(),name='review-list'),
    path('list/<int:pk>/review',ReviewDetailListAV.as_view(),name='watchlist-detail'),
    path('list/<int:pk>/review-create',ReviewCreate.as_view(),name='watchlist-detail'),
    
    
]
