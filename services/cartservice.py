import uuid
from models.order import Order

class CartService:

    def __init__(self, db, payment_gateway):
        self.db = db
        self.payment = payment_gateway

    def checkout(self, user, cart):
        total = 0

        for item in cart.items:
            product = self.db.get_product(item.product_id)
            if not product or not product.has_stock(item.quantity):
                return None
            total += product.price * item.quantity

        for item in cart.items:
            product = self.db.get_product(item.product_id)
            product.stock -= item.quantity

        if not self.payment.charge(user.id, total):
            return None

        order = Order(str(uuid.uuid4()), user.id, cart.items, total)
        order.status = "CONFIRMED"
        self.db.save_order(order)

        return order
