class CartItem:
    """An item in a user's cart."""

    def __init__(self, product_id, quantity):
        self.product_id = product_id
        self.quantity = quantity


class Cart:
    """A user's shopping cart."""

    def __init__(self, cart_id, user_id):
        self.id = cart_id
        self.user_id = user_id
        self.items = []

    def add_item(self, product_id, quantity=1):
        for item in self.items:
            if item.product_id == product_id:
                item.quantity += quantity
                return
        self.items.append(CartItem(product_id, quantity))
