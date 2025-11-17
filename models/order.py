class Order:
    """Represents a successful customer order."""

    def __init__(self, order_id, user_id, items, total):
        self.id = order_id
        self.user_id = user_id
        self.items = items
        self.total = total
        self.status = "PENDING"
