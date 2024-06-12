# inventory/forms.py
from django import forms
from .models import Inventory
from .models import Supplier
from .models import Inbound, Outbound

class ProductForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['id', 'sku', 'name', 'locationid', 'supplierid']

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['supplierid', 'name', 'address']

class InboundForm(forms.ModelForm):
    class Meta:
        model = Inbound
        fields = ['inbid', 'reference', 'date_received', 'product_sku', 'quantity', 'location', 'remarks']

class OutboundForm(forms.ModelForm):
    class Meta:
        model = Outbound
        fields = ['outid', 'reference', 'date_received', 'product_sku', 'quantity', 'location', 'remarks']
