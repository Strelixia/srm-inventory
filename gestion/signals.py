from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Order
from .utils import send_invoice_email, notify_supplier

@receiver(post_save, sender=Order)
def handle_order_status_change(sender, instance, **kwargs):
    if instance.status =='PAID':
        send_invoice_email(instance, buyer_email='murairicedric@gmail.com')
        notify_supplier(instance)