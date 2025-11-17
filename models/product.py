class Product:
    """A product sold in the Elevated Nutrition System."""

    def __init__(self, product_id, name, price, stock=0):
        self.id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def has_stock(self, quantity):
        return self.stock >= quantity
