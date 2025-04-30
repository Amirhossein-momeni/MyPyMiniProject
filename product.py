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
            print("\nProduct List:")
            for p in cls.products:
                print(f"- {p.name:10} : ${p.price}")
