class User:
    """A system user (customer or admin)."""

    def __init__(self, user_id, name, is_admin=False):
        self.id = user_id
        self.name = name
        self.is_admin = is_admin
