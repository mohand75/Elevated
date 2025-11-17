class InventoryService:
    """Admin inventory management."""

    def __init__(self, database):
        self.db = database

    def update_stock(self, product_id, new_stock):
        product = self.db.get_product(product_id)
        if not product:
            return False
        product.stock = new_stock
        self.db.save_product(product)
        return True
