from django.shortcuts import render, redirect
from django.views import View
from . models import Product,Customer_Profile,Cart,Order_Placed
from . forms import CustomerRegistrationForm,Customer_Profile_Form
from django.contrib import messages
from django.contrib.auth import logout
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



# Create your views here.
# Use for Product Show in Home.html
class ProductView(View):
     def get(self,request):
          total_item=0
          Shirt=Product.objects.filter(category='S')
          T_Shirt=Product.objects.filter(category='TS')
          Jeans_Pant=Product.objects.filter(category='JP')
          Normal_Pant=Product.objects.filter(category='P')
          Coat_Tie=Product.objects.filter(category='CT')

          Ladies_T_Shirt=Product.objects.filter(category='LTS')
          Sharee=Product.objects.filter(category='SR')
          Three_Pieces=Product.objects.filter(category='TP')
          Borkah=Product.objects.filter(category='BR')
          Cosmetics=Product.objects.filter(category='C')

          Baby_Toys=Product.objects.filter(category='BT')
          Baby_Fashion=Product.objects.filter(category='BFN')
          Baby_Food=Product.objects.filter(category='BF')

          if request.user.is_authenticated:
               total_item=len(Cart.objects.filter(user=request.user))

          return render(request,'Shop/home.html',{'Shirt':Shirt,'T_Shirt':T_Shirt,'Jeans_Pant':Jeans_Pant,'Normal_Pant':Normal_Pant,'Coat_Tie':Coat_Tie,'Ladies_T_Shirt':Ladies_T_Shirt,'Sharee':Sharee,'Three_Pieces':Three_Pieces,'Borkah':Borkah,'Cosmetics':Cosmetics,'Baby_Toys':Baby_Toys,'Baby_Fashion':Baby_Fashion,'Baby_Food':Baby_Food,'total_item':total_item})


# Use for to Known Product Details
class Product_Details_View(View):
     def get(self,request,pk):
          total_item=0
          product=Product.objects.get(pk=pk)
          item_already_in_cart=False
          if request.user.is_authenticated:
               item_already_in_cart=Cart.objects.filter(Q(product=product.id)  & Q(user=request.user)).exists()
          
               total_item=len(Cart.objects.filter(user=request.user))
          return render(request,'Shop/productdetail.html',{'product':product,'item_already_in_cart': item_already_in_cart,'total_item':total_item})


# Use for Product Show in Category
def Shirt(request,data=None):
     if data==None:
          Shirt=Product.objects.filter(category='S')
     elif data=='Made_in_Bangladesh' or data=='Made_in_India' or data=='Made_in_Malaysia' or data=='Made_in_Singapore' or data=='Made_in_China' or data=='Made_in_Germany' or data=='Made_in_United_States' or data=='Made_in_Canada'or data=='Made_in_UK' :

          Shirt=Product.objects.filter(category='S').filter(brand=data)
     elif data=='below':
          Shirt=Product.objects.filter(category='S').filter(discounted_price__lt=4000)
     elif data=='above':
          Shirt=Product.objects.filter(category='S').filter(discounted_price__gt=4000)    
     return render(request, 'Shop/Shirt.html',{'shirt':Shirt})



def T_Shirt(request,data=None):
     if data==None:
          T_Shirt=Product.objects.filter(category='TS')
     elif data=='Made_in_Bangladesh' or data=='Made_in_India' or data=='Made_in_Malaysia' or data=='Made_in_Singapore' or data=='Made_in_China' or data=='Made_in_Germany' or data=='Made_in_United_States' or data=='Made_in_Canada'or data=='Made_in_UK' :
          T_Shirt=Product.objects.filter(category='TS').filter(brand=data)
     elif data=='below':
          T_Shirt=Product.objects.filter(category='TS').filter(discounted_price__lt=2000)
     elif data=='above':
          T_Shirt=Product.objects.filter(category='TS').filter(discounted_price__gt=2000)    
     return render(request, 'Shop/T_Shirt.html',{'t_shirt':T_Shirt})


def Jeans_Pant(request,data=None):
     if data==None:
          Jeans_Pant=Product.objects.filter(category='JP')
     elif data=='Made_in_Bangladesh' or data=='Made_in_India' or data=='Made_in_Malaysia' or data=='Made_in_Singapore' or data=='Made_in_China' or data=='Made_in_Germany' or data=='Made_in_United_States' or data=='Made_in_Canada'or data=='Made_in_UK' :
          Jeans_Pant=Product.objects.filter(category='JP').filter(brand=data)
     elif data=='below':
          Jeans_Pant=Product.objects.filter(category='JP').filter(discounted_price__lt=3000)
     elif data=='above':
          Jeans_Pant=Product.objects.filter(category='JP').filter(discounted_price__gt=3000)    
     return render(request, 'Shop/Jeans_Pant.html',{'Jeans_Pant':Jeans_Pant})




def Normal_Pant(request,data=None):
     if data==None:
          Normal_Pant=Product.objects.filter(category='P')
     elif data=='Made_in_Bangladesh' or data=='Made_in_India' or data=='Made_in_Malaysia' or data=='Made_in_Singapore' or data=='Made_in_China' or data=='Made_in_Germany' or data=='Made_in_United_States' or data=='Made_in_Canada'or data=='Made_in_UK' :
          Normal_Pant=Product.objects.filter(category='P').filter(brand=data)
     elif data=='below':
          Normal_Pant=Product.objects.filter(category='P').filter(discounted_price__lt=5000)
     elif data=='above':
          Normal_Pant=Product.objects.filter(category='P').filter(discounted_price__gt=5000)    
     return render(request, 'Shop/Normal_Pant.html',{'Normal_Pant':Normal_Pant})


def Coat_Tie(request,data=None):
     if data==None:
          Coat_Tie=Product.objects.filter(category='CT')
     elif data=='Made_in_Bangladesh' or data=='Made_in_India' or data=='Made_in_Malaysia' or data=='Made_in_Singapore' or data=='Made_in_China' or data=='Made_in_Germany' or data=='Made_in_United_States' or data=='Made_in_Canada'or data=='Made_in_UK' :
          Coat_Tie=Product.objects.filter(category='CT').filter(brand=data)
     elif data=='below':
          Coat_Tie=Product.objects.filter(category='CT').filter(discounted_price__lt=30000)
     elif data=='above':
          Coat_Tie=Product.objects.filter(category='CT').filter(discounted_price__gt=30000)    
     return render(request, 'Shop/Coat_Tie.html',{'Coat_Tie':Coat_Tie})


def Ladies_T_Shirt(request,data=None):
     if data==None:
          Ladies_T_Shirt=Product.objects.filter(category='LTS')
     elif data=='Made_in_Bangladesh' or data=='Made_in_India' or data=='Made_in_Malaysia' or data=='Made_in_Singapore' or data=='Made_in_China' or data=='Made_in_Germany' or data=='Made_in_United_States' or data=='Made_in_Canada'or data=='Made_in_UK' :
          Ladies_T_Shirt=Product.objects.filter(category='LTS').filter(brand=data)
     elif data=='below':
          Ladies_T_Shirt=Product.objects.filter(category='LTS').filter(discounted_price__lt=2000)
     elif data=='above':
          Ladies_T_Shirt=Product.objects.filter(category='LTS').filter(discounted_price__gt=2000)    
     return render(request, 'Shop/Ladies_T_Shirt.html',{'Ladies_T_Shirt':Ladies_T_Shirt})


def Sharee(request,data=None):
     if data==None:
          Sharee=Product.objects.filter(category='SR')
     elif data=='Made_in_Bangladesh' or data=='Made_in_India' or data=='Made_in_Malaysia' or data=='Made_in_Singapore' or data=='Made_in_China' or data=='Made_in_Germany' or data=='Made_in_United_States' or data=='Made_in_Canada'or data=='Made_in_UK' :
          Sharee=Product.objects.filter(category='SR').filter(brand=data)
     elif data=='below':
          Sharee=Product.objects.filter(category='SR').filter(discounted_price__lt=2000)
     elif data=='above':
          Sharee=Product.objects.filter(category='SR').filter(discounted_price__gt=2000)    
     return render(request, 'Shop/Sharee.html',{'Sharee':Sharee})


def Three_Pieces(request,data=None):
     if data==None:
          Three_Pieces=Product.objects.filter(category='TP')
     elif data=='Made_in_Bangladesh' or data=='Made_in_India' or data=='Made_in_Malaysia' or data=='Made_in_Singapore' or data=='Made_in_China' or data=='Made_in_Germany' or data=='Made_in_United_States' or data=='Made_in_Canada'or data=='Made_in_UK' :
          Three_Pieces=Product.objects.filter(category='TP').filter(brand=data)
     elif data=='below':
          Three_Pieces=Product.objects.filter(category='TP').filter(discounted_price__lt=25000)
     elif data=='above':
          Three_Pieces=Product.objects.filter(category='TP').filter(discounted_price__gt=25000)    
     return render(request, 'Shop/Three_Pieces.html',{'Three_Pieces':Three_Pieces})



def Borkah(request,data=None):
     if data==None:
          Borkah=Product.objects.filter(category='BR')
     elif data=='Made_in_Bangladesh' or data=='Made_in_India' or data=='Made_in_Malaysia' or data=='Made_in_Singapore' or data=='Made_in_China' or data=='Made_in_Germany' or data=='Made_in_United_States' or data=='Made_in_Canada'or data=='Made_in_UK' :
          Borkah=Product.objects.filter(category='BR').filter(brand=data)
     elif data=='below':
          Borkah=Product.objects.filter(category='BR').filter(discounted_price__lt=10000)
     elif data=='above':
          Borkah=Product.objects.filter(category='BR').filter(discounted_price__gt=10000)    
     return render(request, 'Shop/Borkah.html',{'Borkah':Borkah})



def Cosmetics(request,data=None):
     if data==None:
          Cosmetics=Product.objects.filter(category='C')
     elif data=='Made_in_Bangladesh' or data=='Made_in_India' or data=='Made_in_Malaysia' or data=='Made_in_Singapore' or data=='Made_in_China' or data=='Made_in_Germany' or data=='Made_in_United_States' or data=='Made_in_Canada'or data=='Made_in_UK' :
          Cosmetics=Product.objects.filter(category='C').filter(brand=data)
     elif data=='below':
          Cosmetics=Product.objects.filter(category='C').filter(discounted_price__lt=10000)
     elif data=='above':
          Cosmetics=Product.objects.filter(category='C').filter(discounted_price__gt=10000)    
     return render(request, 'Shop/Cosmetics.html',{'Cosmetics':Cosmetics})



def Baby_Toys(request,data=None):
     if data==None:
          Baby_Toys=Product.objects.filter(category='BT')
     elif data=='Made_in_Bangladesh' or data=='Made_in_India' or data=='Made_in_Malaysia' or data=='Made_in_Singapore' or data=='Made_in_China' or data=='Made_in_Germany' or data=='Made_in_United_States' or data=='Made_in_Canada'or data=='Made_in_UK' :
          Baby_Toys=Product.objects.filter(category='BT').filter(brand=data)
     elif data=='below':
          Baby_Toys=Product.objects.filter(category='BT').filter(discounted_price__lt=10000)
     elif data=='above':
          Baby_Toys=Product.objects.filter(category='BT').filter(discounted_price__gt=10000)    
     return render(request, 'Shop/Baby_Toys.html',{'Baby_Toys':Baby_Toys})



def Baby_Fashion(request,data=None):
     if data==None:
          Baby_Fashion=Product.objects.filter(category='BFN')
     elif data=='Made_in_Bangladesh' or data=='Made_in_India' or data=='Made_in_Malaysia' or data=='Made_in_Singapore' or data=='Made_in_China' or data=='Made_in_Germany' or data=='Made_in_United_States' or data=='Made_in_Canada'or data=='Made_in_UK' :
          Baby_Fashion=Product.objects.filter(category='BFN').filter(brand=data)
     elif data=='below':
          Baby_Fashion=Product.objects.filter(category='BFN').filter(discounted_price__lt=10000)
     elif data=='above':
          Baby_Fashion=Product.objects.filter(category='BFN').filter(discounted_price__gt=10000)    
     return render(request, 'Shop/Baby_Fashion.html',{'Baby_Fashion':Baby_Fashion})




def Baby_Food(request,data=None):
     if data==None:
          Baby_Food=Product.objects.filter(category='BF')
     elif data=='Made_in_Bangladesh' or data=='Made_in_India' or data=='Made_in_Malaysia' or data=='Made_in_Singapore' or data=='Made_in_China' or data=='Made_in_Germany' or data=='Made_in_United_States' or data=='Made_in_Canada'or data=='Made_in_UK' :
          Baby_Food=Product.objects.filter(category='BF').filter(brand=data)
     elif data=='below':
          Baby_Food=Product.objects.filter(category='BF').filter(discounted_price__lt=10000)
     elif data=='above':
          Baby_Food=Product.objects.filter(category='BF').filter(discounted_price__gt=10000)    
     return render(request, 'Shop/Baby_Food.html',{'Baby_Food':Baby_Food})




def product_detail(request):
     return render(request, 'Shop/productdetail.html')

 
@login_required 
def add_to_cart(request):
     user=request.user
     product_id=request.GET.get('prod_id')
     product=Product.objects.get(id=product_id)
     Cart(user=user,product=product).save()
     return redirect('/cart')

     


@login_required
def show_cart(request):
     total_item=0
     if request.user.is_authenticated:
          user=request.user
          cart=Cart.objects.filter(user=user)
          amount=0.0
          shipping_amount=100.0
          total=0.0
          cart_product=[p for p in Cart.objects.all() if p.user==user]
          if cart_product:
               for p in cart_product:
                    temp_amount=(p.quantity * p.product.discounted_price)
                    amount+=temp_amount       # amount = amount + temp_amount
                    total_amount=amount+shipping_amount
               total_item=len(Cart.objects.filter(user=request.user))
               return render(request,'Shop/add_to_cart.html',{'carts':cart,'total_amount':total_amount,'amount':amount,'total_item':total_item})
          else:
               return render(request,'Shop/emptycart.html')

# Plus Cart
def plus_cart(request):
     if request.method=='GET':
          prod_id=request.GET['prod_id']
          c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
          c.quantity +=1
          c.save()
          
          amount=0.0
          shipping_amount=100.0
        
          cart_product=[p for p in Cart.objects.all() if p.user==request.user]

          if cart_product: 
               for p in cart_product:
                    temp_amount=(p.quantity * p.product.discounted_price)
                    amount+=temp_amount       # amount = amount + temp_amount
                    total_amount=amount+shipping_amount
          data={
               'quantity':c.quantity,
               'amount':amount,
               'total_amount':total_amount
          }
          return JsonResponse(data)
     
# Minus Cart
def minus_cart(request):
     if request.method=='GET':
          prod_id=request.GET['prod_id']
          c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
          c.quantity -=1
          c.save()
          
          amount=0.0
          shipping_amount=100.0
        
          cart_product=[p for p in Cart.objects.all() if p.user==request.user]

          if cart_product: 
               for p in cart_product:
                    temp_amount=(p.quantity * p.product.discounted_price)
                    amount+=temp_amount       # amount = amount + temp_amount
                    total_amount=amount+shipping_amount
          data={
               'quantity':c.quantity,
               'amount':amount,
               'total_amount':total_amount
          }
          return JsonResponse(data)


#Remove Cart
def remove_cart(request):
     if request.method=='GET':
          prod_id=request.GET['prod_id']
          c=Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
          
          c.delete()
          
          amount=0.0
          shipping_amount=100.0
        
          cart_product=[p for p in Cart.objects.all() if p.user==request.user]

          if cart_product: 
               for p in cart_product:
                    temp_amount=(p.quantity * p.product.discounted_price)
                    amount+=temp_amount       # amount = amount + temp_amount
                    total_amount=amount+shipping_amount
          data={
               
               'amount':amount,
               'total_amount':total_amount
          }
          return JsonResponse(data)




def buy_now(request):
     return render(request, 'Shop/buynow.html')


@method_decorator(login_required,name='dispatch')
class Profile_View(View):
     def get(self,request):
          form=Customer_Profile_Form
          return render(request,'Shop/Profile.html',{'form':form,'active':'btn-primary'})


     def post(self,request):
          form=Customer_Profile_Form(request.POST)
          if form.is_valid():
               user=request.user
               name=form.cleaned_data['name']
               phone=form.cleaned_data['phone']
               country=form.cleaned_data['country']
               division=form.cleaned_data['division']
               district=form.cleaned_data['district']
               thana=form.cleaned_data['thana']
               vill_or_road=form.cleaned_data['vill_or_road']
               house_name=form.cleaned_data['house_name']
               zipcode=form.cleaned_data['zipcode']

               reg=Customer_Profile(user=user,name=name,phone=phone,country=country,division=division,district=district,thana=thana,vill_or_road=vill_or_road,house_name=house_name,zipcode=zipcode)

               reg.save()
               messages.success(request,'Congratulations! Profile Update Succesfully')
               return render(request, 'Shop/Profile.html',{'form':form})


@login_required
def address(request):
     add=Customer_Profile.objects.filter(user=request.user)
     return render(request, 'Shop/address.html',{'add':add,'active':'btn-primary'})


@login_required
def orders(request):
     op=Order_Placed.objects.filter(user=request.user)
     return render(request, 'Shop/orders.html',{'order_placed':op})


# Use for Create Registration From
class CustomerRegistrationView(View):
     def get(self,request):
          form=CustomerRegistrationForm()
          return render(request, 'Shop/customerregistration.html',{'form':form})
     
     def post(self,request):
          form=CustomerRegistrationForm(request.POST)
          if form.is_valid():
               messages.success(request,'Congratulations Your Registration Successfully done.')
               form.save()
          return render(request, 'Shop/customerregistration.html',{'form':form})


# Use for Logout
def logout_view(request):
     logout(request)
     return redirect('/accounts/login')

@login_required
def checkout(request):
     user=request.user
     add=Customer_Profile.objects.filter(user=user)
     cart_items=Cart.objects.filter(user=user)
     amount=0.0
     shipping_amount=100.0
     total_amount=0.0

     cart_product=[p for p in Cart.objects.all() if p.user==request.user]

     if cart_product: 
               for p in cart_product:
                    temp_amount=(p.quantity * p.product.discounted_price)
                    amount+=temp_amount       # amount = amount + temp_amount
                    total_amount=amount+shipping_amount
     
     return render(request, 'Shop/checkout.html',{'add':add,'total_amount':total_amount,'cart_items':cart_items})



def payment_done(request):
     user = request.user
     custid=request.GET.get('custid')
     customer = Customer_Profile.objects.get(id=custid)
     cart=Cart.objects.filter(user=user)
     for c in cart:
          Order_Placed(user=user,customer=customer,product=c.product,quantity=c.quantity).save()
          c.delete()

     return redirect('orders')


def search(request):
     if request.method=='GET':
          query=request.GET.get('quary')
          if query:
               product=Product.objects.filter(title__icontains=query)
               return render(request,'Shop/search.html',{'product':product})
          else:
               return render(request,'Shop/search.html',{'product':product})

