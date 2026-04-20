from django.contrib import admin
from .models import Product, Order

# Register your product normally
admin.site.register(Product)

# Customize the Order dashboard
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # 1. Shows these specific columns in the main list
    list_display = ['id', 'customer_name', 'status', 'total_price', 'date_ordered']
    
    # 2. Makes the 'status' drop-down editable directly from the main list!
    list_editable = ['status']
    
    # 3. Adds a filter sidebar on the right side of the screen
    list_filter = ['status', 'date_ordered']
    
    # 4. Adds a search bar at the top to find customers quickly
    search_fields = ['customer_name', 'phone_number']
    
    # 5. Makes the cart details read-only so you don't accidentally edit what the customer bought
    readonly_fields = ['items_bought', 'total_price', 'date_ordered']