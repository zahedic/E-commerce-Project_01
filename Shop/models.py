from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Country_Choices

COUNTRY_CHOICES=(
    ('','Select Your Country'),
    ('Bangladesh','Bangladesh'),
    ('India','India'),
    ('Malaysia','Malaysia'),
    ('Singapore','Singapore'),
    ('China','China'),
    ('Germany','Germany'),
    ('United States','United States'),
    ('Canada','Canada'),
    ('UK','UK'),
    
)


# Division_Choices
DIVISION_CHOICES=(
    ('','Select Your Division'),
    ('Barishal','Barishal'),
    ('Chattogram','Chattogram'),
    ('Dhaka','Dhaka'),
    ('Khulna','Khulna'),
    ('Rajshahi','Rajshahi'),
    ('Rangpur','Rangpur'),
    ('Mymensingh','Mymensingh'),
    ('Sylhet','Sylhet'),

    ('Beijing','Beijing'),
    ('Mumbai','Mumbai'),
    ('Delhi','Delhi'),
    ('Berlin','Berlin'),
    ('New York','New York'),
    ('San Francisco','San Francisco'),
    ('Washington DC','Washington DC'),
    ('Toronto','Toronto'),
    ('Ottawa','Ottawa'),
    ('Victoria','Victoria'),
    ('Tokyo','Tokyo'),
    ('Moscow','Moscow'),
    ('Singapore','Singapore'),
    ('Kuala Lumpur','Kuala Lumpur'),
    ('London','London'),
    ('Abu Dhabi','Abu Dhabi'),
    ('Doha','Doha'),
)



class Customer_Profile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    phone=models.IntegerField()
    country=models.CharField(choices=COUNTRY_CHOICES,max_length=200)
    division=models.CharField(choices=DIVISION_CHOICES,max_length=200)
    district=models.CharField(max_length=200)
    thana=models.CharField(max_length=50)
    vill_or_road=models.CharField(max_length=50)
    house_name=models.CharField(max_length=50)
    zipcode=models.IntegerField()


    def __str__(self):
        return str(self.id)
    

CATEGORY_CHOICES=(
    ('S','Shirt'),
    ('TS','T_Shirt'),
    ('JP','Jeans Pant'),
    ('P','Normal Pant'),
    ('CT','Coat Tie'),

    ('LTS','Ladies T-Shirt'),
    ('SR','Sharee'),
    ('TP','Three Pieces'),
    ('BR','Borkah'),
    ('C','Cosmetics'),
   
    ('BT','Baby Toys'),
    ('BFN','Baby Fashion'),
    ('BF','Baby Food'),

)



class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price=models.FloatField()
    description=models.TextField()
    brand=models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=200)
    product_image=models.ImageField(upload_to='product_img')


    def __str__(self):
        return str(self.id)
    

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)


    def __str__(self):
        return str(self.id)
    
    @property
    def product_total_price(self):
        return self.quantity * self.product.discounted_price
    
    

STATUS_CHOICE=(
    ('','Select Your Order'),
    ('Pending','Pending'),
    ('Accepted','Accepted'),
    ('Packed','Packed'),
    ('On the Way','On the Way'),
    ('Delivered','Delivered'),
    ('Cancel','Cancel'),
)




class Order_Placed(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer_Profile,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    ordered_date=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICE,default='Pending')


    def __str__(self):
        return str(self.id)
    
    @property
    def product_total_price(self):
        return self.quantity * self.product.discounted_price
    

  
