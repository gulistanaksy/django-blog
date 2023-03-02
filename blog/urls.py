from django.urls import path, include
from blog.views import iletisim, anasayfa, kategori, yazilarim, detay

urlpatterns = [
    path('', anasayfa, name='anasayfa'),
    path('iletisim',iletisim, name='iletisim'),
    path('anasayfa',anasayfa),
    path('kategori/<slug:kategoriSlug>', kategori, name='kategori'),
    path('yazilarim', yazilarim, name='yazilarim'),
    path('detay/<slug:slug>', detay, name='detay'),
]
