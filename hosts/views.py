from .models import CustomHostUser
from django.views.generic import CreateView,TemplateView,ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from listings.models import HostLists
from .forms import CustomHostUserCreationForm,CustomHostUserChangeForm
from django.urls import reverse_lazy
# Create your views here.

class Signupview(CreateView):
    form_class = CustomHostUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')

class ProfileView(TemplateView):
    template_name = 'HostHome.html'

class HostListings(LoginRequiredMixin,ListView):
    model = HostLists
    template_name = "HostListings.html"
    context_object_name = "listings"

    def get_queryset(self):
        host=self.request.user

        return HostLists.object.filter(listing_host=host)
