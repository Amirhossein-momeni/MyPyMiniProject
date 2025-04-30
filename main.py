class StoreManagement:
    products = []

    def __init__(self, name, price):
        self.name = name
        self.price = price
        StoreManagement.products.append(self)

    @classmethod
    def add_product(cls, name, price):
        if any(p.name == name for p in cls.products):
            print("Product already exists!")
            return
        cls(name, price)
        print(f"'{name}' added successfully.")

    @classmethod
    def delete_item(cls, name_product):
        for product in cls.products:
            if product.name == name_product:
                cls.products.remove(product)
                print(f"'{name_product}' deleted.")
                return
        print("Product not found!")

    @classmethod
    def apply_discount(cls, name_product, discount):
        for product in cls.products:
            if product.name == name_product:
                old_price = product.price
                product.price = product.price * (1 - discount / 100)
                print(f"Discount applied! '{product.name}' price changed from ${old_price} to ${product.price}")
                return
        print("Product not found!")

    @classmethod
    def show_products(cls):
        if not cls.products:
            print("No products available.")
        else:
            print("\n Product List:")
            for p in cls.products:
                print(f"- {p.name:10} : ${p.price}")


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


def menu_admin():
    while True:
        try:
            choice = int(input("\n[ADMIN]\n1) Add Product\n2) Delete Product\n3) Show Products\n4) Apply Discount\n5) Back\n>>> "))
        except ValueError:
            print("Enter a valid number!")
            continue
        if choice == 1:
            name = input("Enter product name: ")
            try:
                price = int(input("Enter product price: "))
            except ValueError:
                print("Price must be a number!")
                continue
            StoreManagement.add_product(name, price)

        elif choice == 2:
            name = input("Enter product name to delete: ")
            StoreManagement.delete_item(name)

        elif choice == 3:
            StoreManagement.show_products()

        elif choice == 4:
            name = input("Enter product name to apply discount: ")
            try:
                discount = int(input("Enter discount percentage: "))
                StoreManagement.apply_discount(name, discount)
            except ValueError:
                print("Discount must be a number!")
                continue

        elif choice == 5:
            break
        else:
            print("Invalid option!")


def menu_buyer(buyer):
    while True:
        try:
            choice = int(input("\n[BUYER]\n1) View Products\n2) Add to Cart\n3) View Cart\n4) Checkout\n5) Back\n>>> "))
        except ValueError:
            print("Enter a valid number!")
            continue
        if choice == 1:
            StoreManagement.show_products()

        elif choice == 2:
            name = input("Enter product name to add to cart: ")
            for product in StoreManagement.products:
                if product.name == name:
                    buyer.add_to_cart(product)
                    break
            else:
                print("Product not found!")

        elif choice == 3:
            buyer.view_cart()

        elif choice == 4:
            buyer.checkout()

        elif choice == 5:
            break
        else:
            print("Invalid option!")


def main_menu():
    while True:
        try:
            x = int(input("\n1) Admin\n2) Buyer\n3) Exit\n>>> "))
        except ValueError:
            continue
        if x == 1:
            menu_admin()
        elif x == 2:
            buyer = BuyStore()
            menu_buyer(buyer)
        elif x == 3:
            print("Goodbye!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main_menu()


