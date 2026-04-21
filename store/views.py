from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to my Django site!")

# --- ADD THIS NEW FUNCTION ---
def product_detail(request, product_id):
    # This finds the exact product by its ID number, or shows a 404 Error if it doesn't exist
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'store/product_detail.html', {'product': product})

# --- SHOPPING CART LOGIC ---

def add_to_cart(request, product_id):
    # Grab the customer's cart from their temporary session, or make a new empty one
    cart = request.session.get('cart', {})
    
    # Session keys must be strings
    product_id_str = str(product_id)
    
    # If the product is already in the cart, add 1 to the quantity. Otherwise, set it to 1.
    if product_id_str in cart:
        cart[product_id_str] += 1
    else:
        cart[product_id_str] = 1
        
    # Save the cart back to the session memory
    request.session['cart'] = cart
    
    # Send the user to the cart page
    return redirect('cart_detail')


def cart_detail(request):
    # Grab the cart from memory
    cart = request.session.get('cart', {})
    
    cart_items = []
    total_price = 0
    
    # Match the memory IDs to actual products in the database
    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        item_total = product.price * quantity
        total_price += item_total
        
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total': item_total
        })
        
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total_price': total_price})
    # store/views.py (add to the bottom)
from .models import Order # Make sure you import Order at the top of the file!

def checkout(request):
    cart = request.session.get('cart', {})
    
    # If the cart is empty, send them back to the homepage
    if not cart:
        return redirect('home')

    if request.method == 'POST':
        # 1. Grab what the customer typed in the form
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        
        # 2. Calculate the total and create a text list of the items
        total_price = 0
        items_string = ""
        
        for product_id, quantity in cart.items():
            product = Product.objects.get(id=product_id)
            total_price += product.price * quantity
            items_string += f"{quantity}x {product.name}\n"
            
            # --- NEW INVENTORY TRACKING ---
            product.stock -= quantity  # Subtract the cart quantity from the database
            product.save()             # Save the new stock number
            # ------------------------------
            
        # 3. Save the new order to the database
        Order.objects.create(
            customer_name=name,
            phone_number=phone,
            shipping_address=address,
            items_bought=items_string,
            total_price=total_price
        )
        
        # 4. Empty the shopping cart
        request.session['cart'] = {}
        
        # 5. Show a success message (we will just reuse the cart page for this quickly)
        return render(request, 'store/cart.html', {'message': 'Order placed successfully! We will contact you for payment.'})

    # If they just loaded the page, show them the form
    return render(request, 'store/checkout.html')