from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,DetailView,ListView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import HostLists
from .forms import HostListForm
from django.urls import reverse_lazy

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

class ListingListView(ListView):
    model = HostLists
    template_name = 'ListingListView.html'

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
