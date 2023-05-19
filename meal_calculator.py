food_price = float(input("\nEnter the cost of the meal: "))
tip_amount = food_price * 18/100
sales_tax_amount = food_price *  7/100
total_amount = food_price + tip_amount + sales_tax_amount

print(f"The price of the meal entered: ${food_price} \n")
print(f"The tip(18% of meal cost): ${tip_amount} \n")
print(f"The sales tax(7% of meal cost): ${sales_tax_amount} \n")
print(f"Grand Total: ${total_amount} \n")