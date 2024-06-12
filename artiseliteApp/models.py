from django.db import models

# Stores locations
class Location(models.Model):
    locationid = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()

#Stores inbound shipment info
class Inbound(models.Model):
    inbid = models.CharField(max_length=50, primary_key=True)
    reference = models.CharField(max_length=50)
    date_received = models.DateTimeField()
    product_sku = models.CharField(max_length=50)
    quantity = models.IntegerField()
    location = models.CharField(max_length=255)
    remarks = models.TextField(blank=True, null=True)

#Stores outbound shipment info
class Outbound(models.Model):
    outid = models.CharField(max_length=50, primary_key=True)
    reference = models.CharField(max_length=50)
    date_shipped = models.DateTimeField()
    product_sku = models.CharField(max_length=50)
    quantity = models.IntegerField()
    destination = models.CharField(max_length=255)
    remarks = models.TextField(blank=True, null=True)

#Stores supplier info
class Supplier(models.Model):
    supplierid = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=255)
    address = models.TextField()

    #Stores inventory information 
class Inventory(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    sku = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    locationid = models.ForeignKey(Location, on_delete=models.CASCADE)
    supplierid = models.ForeignKey(Supplier, on_delete=models.CASCADE)