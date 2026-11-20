# Main.py - Main program management
from Menu import show_menu
from Order import add_order, show_orders
from Billing import calculate_total, calculate_discount, print_invoice


def main():
    while True:
        print("\n========== Coffee Shop ==========")
        print("1. Show menu")
        print("2. Add order")
        print("3. Show orders")
        print("4. Calculate total")
        print("5. Print invoice")
        print("6. Exit")

        choice = input("Your choice: ").strip()

        if choice == "1":
            show_menu()
        elif choice == "2":
            add_order()
        elif choice == "3":
            show_orders()
        elif choice == "4":
            total = calculate_total()
            discount = calculate_discount(total)
            print(f"\n💰 Subtotal: {total:,} Toman")
            print(f"🎁 Discount: {discount:,.0f} Toman")
            print(f"✅ Amount due: {total - discount:,.0f} Toman")
        elif choice == "5":
            print_invoice()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please try again.")


if __name__ == "__main__":
    main()