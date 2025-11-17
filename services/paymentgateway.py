class PaymentGateway:
    """Mock payment processor."""

    def charge(self, user_id, amount):
        # Always succeed for demo
        return True
