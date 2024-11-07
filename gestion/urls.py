from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name='login'),
    path("supplier_dashboard/", views.supplier_dashboard, name="supplier_dashboard"),
    path("buyer_dashboard/", views.buyer_dashboard, name="buyer_dashboard"),
    path("supplier_products/", views.supplier_products, name="supplier_products"),
]



