from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices
# Create your models here.

class user_profile(models.Model):

    STATES = (
        ('TN', 'tamilnadu'),
        ('AP', 'andhra_pradesh'),
        ('TL', 'telangana'),
        ('KA', 'karnataka'),
        ('KL', 'kerala'),
        ('DL', 'delhi'),
        ('MH', 'maharashtra'),
        ('PN', 'punjab'),
        ('RJ', 'rajasthan'),
    )

    CITIES = (
        ('CHN', 'chennai'),
        ('DEL', 'new_Delhi'),
        ('KOL', 'kolkata'),
        ('MUM', 'mumbai'),
        ('BGL', 'bangalore'),
        ('VIZ', 'visakhapatnam'),
        ('HYD', 'hydrabad'),
        ('PUN', 'punjab'),
        ('RAJ', 'rajasthan'),
    )

    TYPE = (
        ('ADM', 'admin'),
        ('SLR', 'seller'),
        ('USR', 'user'),
    )


    #using default User model by linking 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True)
    #additional fields
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    address1 = models.CharField(max_length=100)
    city = models.CharField(max_length=5 , choices=CITIES, blank = True)
    state = models.CharField(max_length=5 , choices=STATES, blank = True)
    postalcode = models.CharField(max_length=6, blank=True)
    country = models.CharField(max_length=20, default="INDIA", blank=True)
    phone = models.CharField(max_length=10, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    type = models.CharField(max_length=5, choices = TYPE, default='ADM')
    website = models.URLField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures' , blank = True )
    bio = models.CharField(blank=True, max_length=300)

    def __str__(self):
        return self.user.username