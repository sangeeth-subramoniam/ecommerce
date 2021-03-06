from django.db import models
from django.contrib.auth.models import User
from django.db.models.aggregates import Count
from PIL import Image
from likes.models import like
from django.core.validators import  MinValueValidator,MaxValueValidator
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
    orderdate = models.DateTimeField(auto_created=True , blank = True)
    totalcost = models.IntegerField(blank=True , default=0)
    shipment_date = models.CharField(max_length=30, default='7 days')
    transactionstatus = models.BooleanField(default=False,blank=True)
    deliverystatus = models.BooleanField(default=False, blank=True)
    deleted = models.BooleanField(default=False, blank=True)
    paymentdate = models.DateTimeField(blank=True)
    order_complete = models.BooleanField(default=False , blank=True)


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
    website = models.URLField(max_length=40)

    def __str__(self):
        return str(self.companyname)


class categories(models.Model):
    categoryid = models.AutoField(primary_key=True)
    categoryname = models.CharField(max_length=30)
    description = models.CharField(max_length=50 , blank=True)
    categorypicture = models.ImageField(upload_to = "category_pictures", blank = True)

    def __str__(self):
        return str(self.categoryname)

    
class products(models.Model):
    productid = models.AutoField(primary_key=True)
    productname = models.CharField(max_length=30)
    productdescription = models.CharField(max_length=50, blank=True)
    supplier = models.ForeignKey(suppliers, on_delete=models.CASCADE)
    category = models.ForeignKey(categories , on_delete= models.CASCADE)
    unit_price = models.IntegerField()
    discount = models.IntegerField(blank=True, default=0)
    instock = models.IntegerField(blank=True)
    available = models.BooleanField(default=True)
    currentorders = models.CharField(max_length=100 , blank=True)
    rank = models.IntegerField(blank=True , default=0)
    picture = models.ImageField(default = 'default.png' , upload_to = "product_pictures" , blank = True)
    likes = models.IntegerField(default=0 , blank=True)
    dislikes = models.IntegerField(default=0 , blank=True)
    created_at = models.DateTimeField(null=True , auto_now_add=True)
    #picture2 = models.ImageField(default = 'default.png' , upload_to = "product_pictures_resized" , blank = True)

    def __str__(self):
        return str(self.productname)

    #def save(self , *args, **kwargs):
    #    super().save(*args, **kwargs)
    #    img = Image.open(self.picture.path)

    #    if img.height != 640 or img.width != 360:
    #        output_size = (640,360)
    #        img.thumbnail(output_size)
    #        img.save(self.picture2.path)


class orderdetails(models.Model):

    DEFAULT_USER_ID = 1

    orderdetailid = models.AutoField(primary_key=True)
    orderdetailnumber = models.IntegerField(blank=True)
    customer = models.ForeignKey(User , on_delete=models.CASCADE , default=DEFAULT_USER_ID)
    order = models.ForeignKey(orders , on_delete=models.CASCADE , blank=True , null = True)
    product = models.ForeignKey(products , on_delete=models.CASCADE)
    price = models.IntegerField()
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    discount = models.IntegerField(blank=True , default=0)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str( str(self.orderdetailid) + ' ' + str(self.product) + ' ' + str(self.quantity))


class reviews(models.Model):
    
    reviewid = models.AutoField(primary_key=True)
    reviewed_by = models.ForeignKey(User , on_delete=models.CASCADE , blank=True , null=True)
    reviewed_product = models.ForeignKey(products , on_delete=models.CASCADE , blank=True , null=True)
    review_title = models.CharField(max_length=30 , blank = True , null=True)
    review_content = models.TextField(max_length=1000 , blank=True, null=True)
    stars = models.DecimalField(default=5 , max_digits=2 , decimal_places=1)
    reviewed_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(str(self.reviewed_by) + str(self.reviewed_product))



