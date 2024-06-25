from .models import CustomHostUser
from django.views.generic import CreateView,TemplateView,ListView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from listings.models import HostLists
from .forms import CustomHostUserCreationForm,CustomHostUserChangeForm
from django.urls import reverse_lazy
# Create your views here.

class Signupview(CreateView):
    form_class = CustomHostUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('login')

class ProfileUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'ProfileUpdate.html'
    model = CustomHostUser
    form_class = CustomHostUserChangeForm

    def get_object(self, queryset=None):
        return self.request.user
    def get_success_url(self):
        return reverse_lazy('hosthome')

class ProfileDeleteView(LoginRequiredMixin,DeleteView):
    template_name = "ProfileDelete.html"
    model = CustomHostUser

    def get_object(self, queryset=None):
        return self.request.user
    def get_success_url(self):
        return reverse_lazy('home')
class ProfileView(TemplateView):
    template_name = 'HostHome.html'

class HostListings(LoginRequiredMixin,ListView):
    model = HostLists
    template_name = "HostListing.html"
    context_object_name = "listings"

    def get_queryset(self):
        host=self.request.user
        return HostLists.objects.filter(listing_host=host)
