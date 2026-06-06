def cart_count(request):
    """Har page pe cart count available karega navbar mein."""
    count = 0
    if request.user.is_authenticated:
        try:
            from .models import Cart
            cart = Cart.objects.filter(user=request.user).first()
            if cart:
                count = sum(i.quantity for i in cart.items.all())
        except Exception:
            count = 0
    return {'cart_count': count}