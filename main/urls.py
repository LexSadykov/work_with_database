from django.contrib import admin
from django.urls import path
from phones import views as phone_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', phone_views.index),
    path('catalog/', phone_views.show_catalog, name='catalog'),
    path('catalog/<slug:slug>/', phone_views.show_product, name='phone'),
]