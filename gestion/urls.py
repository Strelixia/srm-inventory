from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.login_view, name='login'),
    path("logout/", views.logout_view, name='logout'),
    path("supplier_dashboard/", views.supplier_dashboard, name="supplier_dashboard"),
    path("buyer_dashboard/", views.buyer_dashboard, name="buyer_dashboard"),
    path("supplier_products/", views.supplier_products, name="supplier_products"),
    path("delete/product/<int:product_id>/", views.delete_product, name="delete_product"),
    path("edit/product/<int:product_id>/", views.edit_product, name="edit_product"),
    path("buyer_inventory/", views.buyer_inventory, name="buyer_inventory"),
    path("delete/inventory/<int:inventory_id>/", views.delete_inventory, name="delete_inventory"),
    path("edit/inventory/<int:inventory_id>/", views.edit_inventory, name="edit_inventory"),
]



