from product import StoreManagement


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
