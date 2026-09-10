order_amount = int(input("enter the amount :"))

delivery_fees = 0 if order_amount > 300 else 30 

print(f"the delivery fee is: {delivery_fees}")