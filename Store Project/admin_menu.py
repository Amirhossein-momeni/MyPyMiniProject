from product import StoreManagement


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
