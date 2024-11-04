from django.urls import reverse
from django.shortcuts import redirect
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in

@receiver(user_logged_in)
def redirect_user_based_on_role(sender, request, user, **kwargs):
    if user.role  == 'Admin':
        return redirect('admin_dashboard.html')
    elif user.role == 'Supplier':
        return redirect('supplier_dashboard.html')
    elif user.role == 'Buyer':
        return redirect('buyer_dashboard.html')
