from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("login/", views.login_view, name='login'),
    path("logout/", views.logout_view, name='logout'),
    path("supplier_dashboard/", views.supplier_dashboard, name="supplier_dashboard"),
    path("buyer_dashboard/", views.buyer_dashboard, name="buyer_dashboard"),
    path("add_supplier_products/", views.supplier_products, name="supplier_products"),
    path("delete/product/<int:product_id>/", views.delete_product, name="delete_product"),
    path("edit/product/<int:product_id>/", views.edit_product, name="edit_product"),
    path("add_buyer_inventory/", views.buyer_inventory, name="buyer_inventory"),
    path("delete/inventory/<int:inventory_id>/", views.delete_inventory, name="delete_inventory"),
    path("edit/inventory/<int:inventory_id>/", views.edit_inventory, name="edit_inventory"),
    path("add_buyer_orders/", views.buyer_orders, name = "buyer_orders"),
    path("add_supplier_orders/", views.supplier_orders, name = "supplier_orders"),
    path("buyer_payment/<int:order_id>/", views.buyer_payment, name = "buyer_payment"),
    path("supplier_delivery/<int:order_id>", views.supplier_delivery, name = "supplier_delivery"),
    path("buyer_delivery/", views.buyer_delivery, name = "buyer_delivery"),
    path("update_inventory/<int:order_id>", views.update_inventory, name = "update_inventory"),
]



