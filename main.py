from admin_menu import menu_admin
from buyer_menu import menu_buyer
from cart import BuyStore


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
