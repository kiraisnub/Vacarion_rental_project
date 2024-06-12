from django import forms
from .models import HostLists

class HostListForm(forms.ModelForm):
    class Meta:
        model=HostLists
        fields = ['listing_name', 'listing_address', 'listing_price', 'listing_picture1','listing_picture2','listing_picture3']