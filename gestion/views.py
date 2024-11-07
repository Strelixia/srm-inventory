
from django.views.generic import ListView 
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login
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
            
    









    


'''
class ProductView(generic.DetailView):
    model = Product
    template_name = "gestion/product.html"
    def get_queryset(self):
    
        Print all products
    
        return Product.objects.all()
'''
    
