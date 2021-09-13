from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Count
#from payment.models import payment

# Create your models here.

class payment(models.Model):

    PAYMENT_TYPE = (
        ('cash','cash'),
        ('card','card')
    )

    PAYMENT_STATUS = (
        ('paid' , 'paid'),
        ( 'notpaid','notpaid' )
    )

    paymentid = models.AutoField(primary_key=True)
    paymenttype = models.CharField(max_length=10, choices=PAYMENT_TYPE, default='cash')
    status = models.CharField(max_length=10, choices=PAYMENT_STATUS , default='notpaid')


    def __str__(self):
        return str(self.paymentid)


class orders(models.Model):
    orderid = models.AutoField(primary_key=True)
    customerid = models.ForeignKey(User, on_delete=models.CASCADE)
    ordernumber = models.CharField(max_length=100, blank=True)
    paymentid = models.ForeignKey(payment, on_delete=models.CASCADE)
    orderdate = models.DateTimeField(auto_created=True)
    shipment_date = models.CharField(max_length=30, default='7 days')
    transactionstatus = models.BooleanField(default=False,blank=True)
    deliverystatus = models.BooleanField(default=False, blank=True)
    deleted = models.BooleanField(default=False, blank=True)
    paymentdate = models.DateTimeField(blank=True)


    def __str__(self):
        return str(self.orderid)

    
class suppliers(models.Model):
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

    supplierid = models.AutoField(primary_key=True)
    companyname = models.CharField(max_length=50)
    contactname = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=30, choices=CITIES)
    state = models.CharField(max_length=10, choices=STATES)
    postalcode = models.CharField(max_length=6)
    country = models.CharField(max_length=30, default='INDIA')
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=30)
    website = models.URLField(max_length=20)

    def __str__(self):
        return str(self.companyname)
