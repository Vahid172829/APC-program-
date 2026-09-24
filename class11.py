class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, name, price, quantity):
        self.products.append((name, price, quantity))
        print(name, "added to cart.")

    def remove_product(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)
                print(name, "removed from cart.")
                return

        print("Product not found.")

    def total_bill(self):
        total = 0
        for name, price, quantity in self.products:
            total += price * quantity
        return total

    def __del__(self):
        print("Shopping cart object destroyed.")


cart = ShoppingCart("Rahul", "C101")

cart.add_product("Laptop", 50000, 1)
cart.add_product("Mouse", 500, 2)
cart.add_product("Keyboard", 1000, 1)

print("Total Bill: ₹", cart.total_bill())

cart.remove_product("Mouse")

print("Updated Bill: ₹", cart.total_bill())
