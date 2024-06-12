from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
class HostLists(models.Model):
    listing_name=models.CharField(max_length=125)
    listing_address=models.CharField(max_length=250)
    listing_price=models.IntegerField(default=0)
    listing_picture1=models.ImageField(upload_to='listing_pics',blank=False,null=True)
    listing_picture2=models.ImageField(upload_to='listing_pics',blank=False,null=True)
    listing_picture3=models.ImageField(upload_to='listing_pics',blank=True,null=True)
    listing_host = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        # null=False,  # Allow nulls temporarily
    )


    def __str__(self):
        return self.listing_name

    def get_absolute_url(self):
        return reverse('ListingDetail',args=[str(self.id)])

