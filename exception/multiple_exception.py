def process_order(item,quantity):
    try:
       price = {"masala" : 20} [item]
       cost = price * quantity 
       print(f"total cost is {cost}")
    except KeyError:
        print("sorry that chai is not in menu")
    except TypeError:
        print("quantity must be in number")
        
process_order("ginger", 2)
process_order("masala","two")
    