from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views


urlpatterns=[

    path('',views.index,name="index"),
    path('contact', views.contact, name="contact"),
    path('success', views.success, name="success"),
    path('cart',views.cart, name="cart")
       
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)