from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    stock = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
# Leave your Product class alone, just add this to the bottom:

class Order(models.Model):
    # These are the choices you will see in the admin drop-down menu
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    )

    customer_name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    shipping_address = models.TextField()
    items_bought = models.TextField() 
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)
    
    # This is the new field. Every new order will automatically start as 'Pending'
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"