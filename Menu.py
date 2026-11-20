# Menu.py - Coffee shop menu management

menu = {
    "coffee": 80000,
    "tea": 50000,
    "cake": 120000,
    "sandwich": 150000,
    "juice": 60000,
}


def show_menu():
    """Display product names and prices."""
    print("\n========== Coffee Menu ==========")
    print(f"{'Item':<15}{'Price (Toman)':>15}")
    print("-" * 30)
    for item, price in menu.items():
        print(f"{item:<15}{price:>15,}")
    print("-" * 30)