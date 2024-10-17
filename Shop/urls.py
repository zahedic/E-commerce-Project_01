from django.urls import path
from django.conf.urls.static import static
from Shop import views
from .forms import LoginFrom,MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns = [
    path('', views.ProductView.as_view(),name='home'),
    # path('product-detail/', views.product_detail, name='product-detail'),

    path('product-detail/<int:pk>',views.Product_Details_View.as_view(),name='product-detail'),


    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/',views.show_cart, name='show_cart'),

    path('pluscart/',views.plus_cart),

    path('minuscart/',views.minus_cart),

    path('removecart/',views.remove_cart),


    path('buy/', views.buy_now, name='buy-now'),

    path('profile/', views.Profile_View.as_view(), name='profile'),

    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
  
    path('Shirt/', views.Shirt, name='Shirt'),
    path('Shirt/<slug:data>', views.Shirt, name='Shirtitem'),

    path('T_Shirt/', views.T_Shirt, name='T_Shirt'),
    path('T_Shirt/<slug:data>', views.T_Shirt, name='T_Shirtitem'),

    path('Jeans_Pant/', views.Jeans_Pant, name='Jeans_Pant'),
    path('Jeans_Pant/<slug:data>', views.Jeans_Pant, name='Jeans_Pant_item'),

    path('Normal_Pant/', views.Normal_Pant, name='Normal_Pant'),
    path('Normal_Pant/<slug:data>', views.Normal_Pant, name='Normal_Pant_item'),


    path('Coat_Tie/', views.Coat_Tie, name='Coat_Tie'),
    path('Coat_Tie/<slug:data>', views.Coat_Tie, name='Coat_Tie_item'),


    path('Ladies_T_Shirt/', views.Ladies_T_Shirt, name='Ladies_T_Shirt'),
    path('Ladies_T_Shirt/<slug:data>', views.Ladies_T_Shirt, name='Ladies_T_Shirt_item'),


    path('Sharee/', views.Sharee, name='Sharee'),
    path('Sharee/<slug:data>', views.Sharee, name='Sharee_item'),


    path('Three_Pieces/', views.Three_Pieces, name='Three_Pieces'),
    path('Three_Pieces/<slug:data>', views.Three_Pieces, name='Three_Pieces_item'),


    path('Borkah/', views.Borkah, name='Borkah'),
    path('Borkah/<slug:data>', views.Borkah, name='Borkah_item'),

    path('Cosmetics/', views.Cosmetics, name='Cosmetics'),
    path('Cosmetics/<slug:data>', views.Cosmetics, name='Cosmetics_item'),


    path('Baby_Toys/', views.Baby_Toys, name='Baby_Toys'),
    path('Baby_Toys/<slug:data>', views.Baby_Toys, name='Baby_Toys_item'),

    path('Baby_Fashion/', views.Baby_Fashion, name='Baby_Fashion'),
    path('Baby_Fashion/<slug:data>', views.Baby_Fashion, name='Baby_Fashion_item'),

    path('Baby_Fashion/', views.Baby_Fashion, name='Baby_Fashion'),
    path('Baby_Fashion/<slug:data>', views.Baby_Fashion, name='Baby_Fashion_item'),

    path('Baby_Food/', views.Baby_Food, name='Baby_Food'),
    path('Baby_Food/<slug:data>', views.Baby_Food, name='Baby_Food_item'),

    #path('login/', views.login, name='login'),

    path('accounts/login/',auth_views.LoginView.as_view(template_name='Shop/login.html',authentication_form=LoginFrom),name='login'),

    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),

    path('logout/',views.logout_view,name='logout'),


    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='Shop/changepassword.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone'),name='passwordchange'),


    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='Shop/password_change_done.html'),name='passwordchangedone'),


    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='Shop/password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),

    path('password_reset/done',auth_views.PasswordResetDoneView.as_view(template_name='Shop/password_reset_done.html'),name='password_reset_done'),

    path('password_reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='Shop/password_reset_complete.html'),name='password_reset_complete'),


 
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='Shop/password_reset_confirm.html'),name='password_reset_confirm'),

    path('checkout/', views.checkout, name='checkout'),


    path('paymentdone/',views.payment_done,name='paymentdone'),

    path('search/',views.search,name='search_item'),

    #path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),

    #path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



