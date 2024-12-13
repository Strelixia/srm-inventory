from django.contrib import messages
from django.views.generic import ListView 
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from functools import wraps
from .models import User, Product, Inventory, Order, Payment, Delivery
from .utils import send_invoice_email, send_delivery_email
def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login (request, user)
            
            if user.role == 'Supplier':
                return redirect( 'supplier_dashboard')
            elif user.role == 'Buyer':
                return redirect( 'buyer_dashboard')
        
        else: 
            return render(request,'login.html',{'error': 'invalid username or password'})
    return render(request, 'login.html')

def role_required(role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
                if request.user.is_authenticated and request.user.role == role:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponseForbidden(" NO PERMISSION")
        return _wrapped_view
    return decorator 

@login_required
@role_required('Supplier')
def supplier_dashboard(request):
    return render(request, 'supplier_dashboard.html')

@login_required
@role_required('Buyer')
def buyer_dashboard(request):
    return render(request, 'buyer_dashboard.html')

@login_required
@role_required('Supplier')
def supplier_products(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        print(name,description,price, quantity)
        Product.objects.create(name = name,description = description,price = price, quantity = quantity, supplier = request.user)
        return redirect('supplier_products')
    products = Product.objects.all()
    return render(request, 'supplier_products.html', {'products': products})         

@login_required
@role_required('Supplier')
def delete_product(request, product_id):
    product = get_object_or_404(Product, id =product_id)
    if request.method =='POST':
        product.delete()
        return redirect('supplier_products')

@login_required  
@role_required('Supplier')
def edit_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method =='POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        product.name = name
        product.description= description
        product.price= price
        product.save()
        return redirect('supplier_products')
    return render(request, 'edit_product.html', {'product': product})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
@role_required('Buyer')
def buyer_inventory(request):
    if request.method =='POST':
        product_id = request.POST.get('product')
        quantity = int(request.POST.get('quantity'))
        product = Product.objects.get(id = product_id)
        if product_id and quantity:
            
            existing_inventory = Inventory.objects.filter(product_id = product_id, user = request.user).first()
            if existing_inventory:
                existing_inventory.quantity += quantity
                existing_inventory.save()
            else:
                inventory = Inventory.objects.create(product = product, quantity = quantity, user = request.user)
        return redirect('buyer_inventory')
    
    products = Product.objects.all()
    inventory = Inventory.objects.all()
    return render(request, 'buyer_inventory.html',{'products': products,'inventory': inventory})

@login_required
@role_required('Buyer')
def delete_inventory(request, inventory_id):
    inventory = get_object_or_404(Inventory, id = inventory_id)
    if request.method =='POST':
        inventory.delete()
        return redirect('buyer_inventory')

@login_required
@role_required('Buyer')
def edit_inventory(request, inventory_id):
    inventory = get_object_or_404(Inventory, id = inventory_id)
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        inventory.quantity = quantity
        inventory.save()
        return redirect('buyer_inventory')
    return render(request,'edit_inventory.html', {'inventory': inventory} )

@login_required
@role_required('Buyer')
def buyer_orders(request):
    if request.method == 'POST':
        order_date = datetime.date.today()
        product_id = request.POST.get('product')
        quantity = int(request.POST.get('quantity'))
        product = Product.objects.get(id = product_id)
        
        if product.quantity < quantity:
            messages.error(request,f" Quantity's not available, we have {product.quantity}")
            return redirect('buyer_orders')
        Order.objects.create(product = product,quantity = quantity,  order_date = order_date, buyer = request.user)
        return redirect('buyer_orders')
    
    pending_orders = Order.objects.filter(status = 'PENDING')
    paid_orders = Order.objects.filter(status = 'PAID')
    products = Product.objects.all()
    return render(request, 'buyer_orders.html', {'products': products,'pending_orders': pending_orders, 'paid_orders': paid_orders,})
    

@login_required
@role_required('Supplier')
def supplier_orders(request):
    if request.method == 'POST':
        order_date = datetime.date.today()
        product_id = request.POST.get('product')
        quantity = request.POST.get('quantity')
        product = Product.objects.get(id = product_id)
        print(order_date, quantity)
        Order.objects.create(product = product,quantity = quantity,  order_date = order_date, buyer = request.user, supplier = request.user)
        return redirect('supplier_orders')
    paid_orders =  Order.objects.filter(status ='PAID')
    delivery_orders = Order.objects.filter(status ='DELIVERED')
    products = Product.objects.all()
    return render(request, 'supplier_orders.html', {'products': products,'delivery_orders': delivery_orders, 'paid_orders': paid_orders})

@login_required  
@role_required('Buyer')
def buyer_payment(request, order_id):
    order = get_object_or_404(Order, id = order_id)
    amount = order.quantity * order.product.price
    if request.method == 'POST':
        payment_date = datetime.datetime.now()
        Payment.objects.create( order = order, amount = amount)
        order.status = ('PAID')
        order.payment_date = payment_date
        order.save()
        send_invoice_email(order, buyer_email ='murairicedric@gmail.com',supplier_email = 'maguy.birikomo@gmail.com')
        return redirect('buyer_orders')
    return render(request, 'buyer_payment.html',{'order': order,'amount': amount})

@login_required
@role_required('Buyer')
def delete_order(request, order_id):
    order = get_object_or_404(Order, id = order_id)
    if request.method =='POST':
        order.delete()
        return redirect('buyer_orders')
    

@login_required  
@role_required('Supplier')
def supplier_delivery(request, order_id):
    order = get_object_or_404(Order, id = order_id)
    amount = order.quantity * order.product.price
    
    if request.method == 'POST':
        delivery_date = datetime.datetime.now()
        Delivery.objects.create( order = order)
        order.status = ('DELIVERED')
        order.delivery_date = delivery_date
        order.save()
        order.product.quantity -= order.quantity
        order.product.save()
        send_delivery_email(order, buyer_email ='murairicedric@gmail.com', supplier_email = 'maguy.birikomo@gmail.com')
        return redirect('supplier_orders')
    return render(request, 'supplier_delivery.html',{'order': order, 'amount': amount})

@login_required  
@role_required('Buyer')
def buyer_delivery(request):
    if request.method == 'POST':
        order_date = datetime.date.today()
        product_id = request.POST.get('product')
        quantity = request.POST.get('quantity')
        product = Product.objects.get(id = product_id)
        print(order_date, quantity)
        Order.objects.create(product = product,quantity = quantity,  order_date = order_date, buyer = request.user, supplier = request.user)
        return redirect('buyer_delivery')
    paid_orders =  Order.objects.filter(status ='PAID')
    delivery_orders = Order.objects.filter(status ='DELIVERED', is_processed = False)
    products = Product.objects.all()
    return render (request, 'buyer_delivery.html', {'products': products,'delivery_orders': delivery_orders, 'paid_orders': paid_orders})

@login_required  
@role_required('Buyer')
def update_inventory(request, order_id):
    order = get_object_or_404(Order, id= order_id)
    product = order.product
    quantity = order.quantity
    if request.method == 'POST':
        existing_inventory = Inventory.objects.filter(product = product, user = request.user).first()
        if existing_inventory:
            existing_inventory.quantity += quantity
            existing_inventory.save()
        else:
            Inventory.objects.create(product = product, quantity = quantity, user = request.user)
        order.is_processed = True
        order.save()
        return redirect('buyer_inventory')
    return render(request, 'buyer_delivery.html')

