
from django.views.generic import CreateView
from .forms import CustomHostUserCreationForm
from django.urls import reverse_lazy
# Create your views here.

class Signupview(CreateView):
    form_class = CustomHostUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')
