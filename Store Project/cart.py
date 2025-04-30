class BuyStore:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)
        print(f"'{product.name}' added to cart.")

    def remove_from_cart(self, name_product):
        for product in self.cart:
            if product.name == name_product:
                self.cart.remove(product)
                print(f"'{name_product}' removed from cart.")
                return
        print("Product not found in cart!")

    def view_cart(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("\nShopping Cart:")
            total = 0
            for p in self.cart:
                print(f"- {p.name:10} : ${p.price}")
                total += p.price
            print(f"Total: ${total}")

    def checkout(self):
        total = 0
        if not self.cart:
            print("Your cart is empty! Add items first.")
        else:
            print("\nCheckout:")
            for p in self.cart:
                print(f"- {p.name:10} : ${p.price}")
                total += p.price
            print(f"Total: ${total}")
            print("Checkout successful!")
