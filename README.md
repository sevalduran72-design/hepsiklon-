# Hepsiburada Klonu - Django E-Ticaret Projesi 🛒

Bu proje, Python ve Django framework'ü kullanılarak geliştirilmiş, tam kapsamlı (full-stack) bir e-ticaret web uygulamasıdır. 

## 🚀 Özellikler

- **Kullanıcı Yetkilendirme (Auth):** Güvenli kayıt olma, giriş yapma ve çıkış yapma sistemleri.
- **Sepet Sistemi:** Oturumlara (sessions) dayalı, anlık güncellenen alışveriş sepeti altyapısı.
- **Sipariş Tamamlama (Checkout):** Sepetteki ürünlerin tutar hesaplaması ve sipariş sonlandırma simülasyonu.
- **Dinamik Ürün Vitrini:** Veritabanından çekilen ürünlerin anlık olarak ana sayfada listelenmesi.
- **Responsive Tasarım:** Tüm cihazlarla uyumlu, modern arayüz (Bootstrap 5 & Custom CSS).

## 🛠️ Kullanılan Teknolojiler

- **Backend:** Python, Django
- **Frontend:** HTML5, CSS3, Bootstrap 5, FontAwesome
- **Veritabanı:** SQLite3
- **Versiyon Kontrolü:** Git & GitHub

## ⚙️ Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyebilirsiniz:

1. Depoyu klonlayın:
   `git clone <sizin-github-repo-linkiniz>`
2. Sanal ortam (virtual environment) oluşturun ve aktifleştirin.
3. Gerekli kütüphaneleri kurun (Django).
4. Veritabanı tablolarını oluşturun:
   `python manage.py migrate`
5. Sunucuyu başlatın:
   `python manage.py runserver`