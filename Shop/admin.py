from django.contrib import admin

from .models import(
    Customer_Profile,
    Product,
    Cart,
    Order_Placed

)

# Register your models here.

@admin.register(Customer_Profile)
class CustomerProfileModelAdmin(admin.ModelAdmin):
    list_display=['id','user','name','phone','country','division','district','thana','vill_or_road','house_name','zipcode']



@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id','title','selling_price','discounted_price','description','brand','category','product_image']



@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']


@admin.register(Order_Placed)
class Order_PlacedModelAdmin(admin.ModelAdmin):
    list_display=['id','user','customer','product','quantity','ordered_date','status']



