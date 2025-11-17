from models.product import Product
from models.user import User
from models.cart import Cart
from services.database import Database
from services.cartservice import CartService
from services.paymentgateway import PaymentGateway
from services.inventoryservice import InventoryService

db = Database()

db.save_product(Product("p1", "Protein Bar", 3.50, 50))
db.save_product(Product("p2", "Vitamin Water", 2.00, 30))

user = User("u1", "Mo")

cart = Cart("c1", user.id)
cart.add_item("p1", 2)
cart.add_item("p2", 1)

cart_service = CartService(db, PaymentGateway())

order = cart_service.checkout(user, cart)

if order:
    print("Order Confirmed:", order.id, "Total:", order.total)
else:
    print("Order Failed")

admin = User("admin1", "Admin", True)
inventory = InventoryService(db)
inventory.update_stock("p1", 100)
