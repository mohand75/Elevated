class Database:
    """A simple in-memory database."""

    def __init__(self):
        self.products = {}
        self.orders = {}

    def save_product(self, product):
        self.products[product.id] = product

    def get_product(self, product_id):
        return self.products.get(product_id)

    def save_order(self, order):
        self.orders[order.id] = order
