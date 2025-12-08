# Below are functions to calculate percentages and apply discounts.
def apply_discount(total_amount, discount_percentage):
    """
    Returns the final amount after deducting the discount percentage.
    """
    if discount_percentage < 0 or discount_percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100.")

    discount_value = total_amount * (discount_percentage / 100)
    final_amount = total_amount - discount_value
    return final_amount

total = float(input("Enter the total amount: "))
discount = float(input("Enter the discount percentage: "))
final_price = apply_discount(total, discount)
saved_amount = total - final_price
print(f"The final price after discount is: £{final_price:.2f}")
print(f"You saved: £{saved_amount:.2f}")
