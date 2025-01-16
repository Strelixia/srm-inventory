from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from .utils import send_email

@receiver(post_save, sender=Order)
def handle_order_status_change(sender, instance, **kwargs):
    if instance.status =='PAID':
        send_email(instance, buyer_email='murairicedric@gmail.com', supplier_email ='maguy.birikomo@gmail.com')