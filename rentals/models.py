#from django.conf import settings
from django.db import models
from django.urls import reverse
from users.models import CustomUser
#from application.models import Application

class Property(models.Model):
    property_id = models.AutoField(primary_key= True)
    rent = models.DecimalField("Rent", max_digits=6,decimal_places=2)
    num_bed = models.SmallIntegerField("Number of Bedrooms")
    num_bath = models.SmallIntegerField("Number of Bathrooms")
    address = models.CharField("Address", max_length=50)
    TYPE_CHOICES =(
    ('1', 'Apartment'),
    ('2', 'House'),
    ('3', 'Douplex'),
    ('4', 'Condo'))
    p_type = models.CharField("Property Type", max_length=20, choices= TYPE_CHOICES)
    desc = models.TextField("Description", max_length=500)
    photo = models.ImageField("Photo", upload_to='static/media/images')
    url = models.CharField(max_length=200)

    def __str__(self):
        return f"Photo for cat_id: {self.cat_id} @{self.url}"

    def __str__(self):
        return (self.address)
    def get_absolute_url(self):
        return reverse('rental_detail', args=[str(self.pk)])
        
class PropertyPhoto(models.Model):
    propty= models.ForeignKey(Property, on_delete = models.CASCADE)
    title = models.TextField(null = True, blank = True)
    photo= models.ImageField("Browse photo to upload", upload_to='static/media/images/propertydetail', blank= True, null= True)
    url = models.CharField(max_length=200)

    def __str__(self):
        return f"Photo for cat_id: {self.cat_id} @{self.url}"


# Create your models here.
