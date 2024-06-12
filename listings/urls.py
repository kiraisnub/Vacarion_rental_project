from django.urls import path
from django.http.response import responses
from .views import HomeView,CreateLisitngView,DetailLisitngView,ListingListView,ListingUpdateView,ListingDeleteView
urlpatterns=[
    path('',HomeView.as_view(),name='home'),
    path('listings/<int:pk>',DetailLisitngView.as_view(),name='ListingDetail'),
    path('listings/<int:pk>/edit',ListingUpdateView.as_view(),name='ListingUpdate'),
    path('listings/<int:pk>/delete',ListingDeleteView.as_view(),name='ListingDelete'),
    path('listings/new/',CreateLisitngView.as_view(),name='CreateListing'),
    path('listings/',ListingListView.as_view(),name='ListingListView'),
]