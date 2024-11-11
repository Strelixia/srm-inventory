
from django.views.generic import ListView 
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from .models import User, Product, Inventory, Order, Payment, Delivery





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

@login_required
def supplier_dashboard(request):
    return render(request, 'supplier_dashboard.html')

@login_required
def buyer_dashboard(request):
    return render(request, 'buyer_dashboard.html')
@login_required
def supplier_products(request):
    if request.method == "POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        print(name,description,price)
        Product.objects.create(name = name,description = description,price = price, supplier = request.user)
        return redirect('supplier_products')
    products = Product.objects.all()
        
    return render(request, 'supplier_products.html', {'products': products})         

@login_required
def delete_product(request, product_id):
    product = get_object_or_404(Product, id =product_id)
    if request.method =='POST':
        product.delete()
        return redirect('supplier_products')
    
@login_required
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
def buyer_inventory(request):
    if request.method =='POST':
        product_id = request.POST.get('product')
        quantity = request.POST.get('quantity')
        product =Product.objects.get(id = product_id)
        if product == product_id:
            quantity += quantity
        print(product, quantity) 
        inventory = Inventory.objects.create(product = product, quantity = quantity, user = request.user)
        return redirect('buyer_inventory')
    products = Product.objects.all()
    inventory = Inventory.objects.all()
    return render(request, 'buyer_inventory.html',{'products': products,'inventory': inventory})


@login_required
def delete_inventory(request, inventory_id):
    product = get_object_or_404(Inventory, id =inventory_id)
    if request.method =='POST':
        product.delete()
        return redirect('buyer_inventory')


