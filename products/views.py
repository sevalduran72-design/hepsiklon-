from django.shortcuts import render, redirect
from .models import Product
# YENİ EKLENENLER: Django'nun hazır güvenlik ve form kütüphaneleri
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def product_list(request):
    products = Product.objects.all()
    cart = request.session.get('cart', {})
    cart_count = sum(cart.values()) 
    return render(request, 'products/product_list.html', {
        'products': products, 
        'cart_count': cart_count
    })

def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1
    request.session['cart'] = cart
    return redirect('home')

def cart_detail(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total_price = 0
    for product_id, quantity in cart.items():
        product = Product.objects.filter(id=product_id).first()
        if product:
            subtotal = product.price * quantity
            total_price += subtotal
            cart_items.append({
                'product': product,
                'quantity': quantity,
                'subtotal': subtotal
            })
    return render(request, 'products/cart_detail.html', {
        'cart_items': cart_items,
        'total_price': total_price
    })

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id_str = str(product_id)
    if product_id_str in cart:
        del cart[product_id_str]
    request.session['cart'] = cart
    return redirect('cart_detail')

def checkout(request):
    request.session['cart'] = {}
    return render(request, 'products/checkout.html')

# --- YENİ EKLENEN KULLANICI SİSTEMİ KODLARI ---

def register_request(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() # Kullanıcıyı veritabanına kaydet
            login(request, user) # Kayıt olunca müşteriye otomatik giriş yaptır
            return redirect("home")
    else:
        form = UserCreationForm()
    return render(request, "products/register.html", {"form": form})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "products/login.html", {"form": form})

def logout_request(request):
    logout(request)
    return redirect("home")