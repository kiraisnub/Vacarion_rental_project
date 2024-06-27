from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,DetailView,ListView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import HostLists
from .forms import HostListForm
from django.urls import reverse_lazy


import pandas as pd

class Func():
    def __init__(self):
        self.df = pd.read_csv('D:\CODING\python\django/vacation_rentel_pro\listings\in.csv')
        self.cities_in_india = self.df['City'].tolist()


city_list=Func().cities_in_india
from django.contrib.auth import get_user_model
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class CreateLisitngView(LoginRequiredMixin,CreateView):
    model = HostLists
    template_name = 'CreateListing.html'
    form_class = HostListForm
    login_url = 'login'

    def form_valid(self, form):
        form.instance.listing_host=self.request.user
        return super().form_valid(form)

    # fields = ('listing_name','listing_address','listing_price','listing_picture1','listing_picture2','listing_picture3','listing_host')

class DetailLisitngView(LoginRequiredMixin,DetailView):
    model = HostLists
    template_name = 'ListingDetail.html'
    login_url = 'login'

# class ListingListView(ListView):
#
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#
#         # Apply sorting based on URL parameter
#         sort_option = self.request.GET.get('sort', '')
#         if sort_option == 'price_low_to_high':
#             queryset = queryset.order_by('listing_price')
#         elif sort_option == 'price_high_to_low':
#             queryset = queryset.order_by('-listing_price')
#
#         # Apply city filter based on URL parameter, only if city is not empty
#         city_option = self.request.GET.get('city', '').strip()
#         if city_option:
#             queryset = queryset.filter(listing_city__iexact=city_option)
#
#         return queryset
#


class ListingListView(ListView):
    model = HostLists
    template_name = 'ListingListView.html'


    def get_queryset(self):
        queryset = super().get_queryset()

        # Apply sorting based on URL parameter
        sort_option = self.request.GET.get('sort', '')
        if sort_option == 'price_low_to_high':
            queryset = queryset.order_by('listing_price')
        elif sort_option == 'price_high_to_low':
            queryset = queryset.order_by('-listing_price')

        # Apply city filter based on URL parameter, only if city is not empty
        city_option = self.request.GET.get('city', '').strip()
        if city_option:
            queryset = queryset.filter(listing_city__iexact=city_option)

        return queryset

class ListingUpdateView(UserPassesTestMixin,UpdateView):
    model = HostLists
    fields = ('listing_name', 'listing_price', 'listing_picture1','listing_picture2','listing_picture3')
    template_name = 'ListingUpdate.html'
    def test_func(self):
        obj=self.get_object()
        return obj.listing_host==self.request.user

class ListingDeleteView(UserPassesTestMixin,DeleteView):
    model = HostLists
    template_name = 'ListingDelete.html'
    success_url = reverse_lazy('ListingListView')

    def test_func(self):
        obj=self.get_object()
        return obj.listing_host==self.request.user
