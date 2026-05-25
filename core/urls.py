from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Bütün fonksiyonlarımızı buraya dahil ettik
from products.views import (
    product_list, add_to_cart, cart_detail, remove_from_cart, checkout,
    register_request, login_request, logout_request
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='home'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_detail, name='cart_detail'),
    path('remove-from-cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    
    # YENİ EKLENEN KULLANICI YOLLARI
    path('register/', register_request, name='register'),
    path('login/', login_request, name='login'),
    path('logout/', logout_request, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)