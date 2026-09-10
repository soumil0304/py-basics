def calculate_bill(cups, price_per_cup):
    return cups*price_per_cup
my_bill=calculate_bill(3, 15)
print(my_bill)
print(f"order for table no 2 is : ",calculate_bill(2, 50))