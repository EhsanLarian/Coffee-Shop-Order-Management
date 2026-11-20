# Order.py - Order management
from Menu import menu

# List of orders; each order is a dictionary
orders = []


def add_order():
    """Get item name and quantity from the user and save the order."""
    item = input("Enter the item name: ").strip().lower()

    if item not in menu:
        print(f"❌ Item '{item}' is not available on the menu!")
        return

    try:
        quantity = int(input("Enter the quantity: "))
        if quantity <= 0:
            print("❌ Quantity must be a positive number.")
            return
    except ValueError:
        print("❌ Invalid quantity entered.")
        return

    order = {
        "item": item,
        "price": menu[item],
        "quantity": quantity,
    }
    orders.append(order)
    print(f"✅ Order for '{item}' (quantity: {quantity}) has been added.")


def show_orders():
    """Display all registered orders."""
    if not orders:
        print("📭 No orders have been placed yet.")
        return

    print("\n========== Registered Orders ==========")
    print(f"{'#':<4}{'Item':<15}{'Price':>12}{'Qty':>8}")
    print("-" * 40)
    for i, order in enumerate(orders, start=1):
        print(
            f"{i:<4}{order['item']:<15}"
            f"{order['price']:>12,}{order['quantity']:>8}"
        )
    print("-" * 40)