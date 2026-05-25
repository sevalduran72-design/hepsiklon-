from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Ürün Adı")
    description = models.TextField(verbose_name="Ürün Açıklaması")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Fiyat")
    stock = models.IntegerField(default=0, verbose_name="Stok Miktarı")
    image = models.ImageField(upload_to='products/', null=True, blank=True, verbose_name="Ürün Görseli")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Eklenme Tarihi")

    # Bu kısım, ürünün sistemde "Object 1" yerine kendi adıyla (örn: iPhone 15) görünmesini sağlar
    def __str__(self):
        return self.name