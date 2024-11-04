
from django.views import generic
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



@login_required(login_url='/login/')
def supplier_dashboard(request):
    return render(request, 'supplier_dashboard.html')

@login_required(login_url='/login/')
def buyer_dashboard(request):
    return render(request, 'buyer_dashboard.html')


'''   
def user_list(request):
    users = User.objects.all()
    return render (request, 'gestion/user_list.html', {'users': users})

def user_detail(request, user_id):
    user = get_object_or_404(User, id= user_id)
    return render(request, 'gestion/user_detail.html', {'user': user})

def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_List')
    else:
        form = UserForm()
    return render(request, 'gestion/user_form.html', {'form': form})
    
def user_update(request, user_id):
    user = get_object_or_404(User, id= user_id)
    if request.method =='POST':
        form = UserForm(request.POST, instance= user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        else:
            form = UserForm(instance = user)
        return render (request, 'gestion/user_form.html', {'form': form})
    
def user_delete(request, user_id):
    user = get_object_or_404(User, id= user_id)
    if request.method =='POST':
        user.delete()
        return redirect ('user_list')
    return render(request, 'gestion/user_confirm_delete.html', {'user': user})
    

class ProductView(generic.DetailView):
    model = Product
    template_name = "gestion/product.html"
    def get_queryset(self):
        """
        Print all products
        """
        return Product.objects.all()
        '''
    
