# Billing.py - Cost calculation and invoice generation
from Order import orders


def calculate_total():
    """Calculate the total cost of all orders."""
    total = 0
    for order in orders:
        total += order["price"] * order["quantity"]
    return total


def calculate_discount(total):
    """Calculate discount: 10% for totals above 1,000,000 Toman."""
    if total > 1_000_000:
        return total * 0.10
    return 0


def print_invoice():
    """Display the final invoice."""
    if not orders:
        print("📭 There are no orders to generate an invoice for.")
        return

    print("\n========== Invoice ==========")
    print(f"{'Item':<15}{'Qty':>8}{'Unit Price':>15}{'Total':>15}")
    print("-" * 55)

    for order in orders:
        line_total = order["price"] * order["quantity"]
        print(
            f"{order['item']:<15}{order['quantity']:>8}"
            f"{order['price']:>15,}{line_total:>15,}"
        )

    print("-" * 55)

    total = calculate_total()
    discount = calculate_discount(total)
    final = total - discount

    print(f"{'Subtotal:':<40}{total:>15,}")
    print(f"{'Discount:':<40}{discount:>15,.0f}")
    print(f"{'Final Amount Due:':<40}{final:>15,.0f}")
    print("=" * 55)