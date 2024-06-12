# inventory/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm, SupplierForm, InboundForm
from .models import Supplier, Inbound, Outbound, Inventory

def managerhome(request):
    return render(request, 'pages/managerhome.html')

def operatorhome(request):
    return render(request, 'pages/operatorhome.html')

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_products')
    else:
        form = ProductForm()
    return render(request, 'pages/add_product.html', {'form': form})

def view_products(request):
    products = Inventory.objects.all()
    return render(request, 'pages/view_products.html', {'products': products})

def update_product(request, pk):
    product = get_object_or_404(Inventory, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('view_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'pages/update_product.html', {'form': form})

def search_products(request):
    query = request.GET.get('query')
    results = []
    if query:
        results = Inventory.objects.filter(name__icontains=query) | Inventory.objects.filter(tags__icontains=query)
    return render(request, 'pages/search_products.html', {'results': results, 'query': query})

def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier_list')  # Redirect to supplier list page
    else:
        form = SupplierForm()
    return render(request, 'inbound/add_supplier.html', {'form': form})

def add_incoming_product(request):
    if request.method == 'POST':
        form = InboundForm(request.POST)
        if form.is_valid():
            form.save()
            # Update inventory here
            return redirect('incoming_product_list')  # Redirect to incoming product list page
    else:
        form = InboundForm()
    return render(request, 'inbound/add_incoming_product.html', {'form': form})

def view_incoming_products(request):
    incoming_products = Inbound.objects.all()
    return render(request, 'incoming/view_incoming.html', {'incoming_products': incoming_products})

def view_outgoing_products(request):
    view_outgoing_products = Outbound.objects.all()
    return render(request, 'outbound/view_outbound.html', {'outbound_products': view_outgoing_products})
