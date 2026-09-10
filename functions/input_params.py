# chai = "ginger chai"


# def prepare_chai(order):
#     print("preparing", order)


# prepare_chai = chai
# print(chai)

chai = [1, 2, 3]


def edit_chai(cup):
    cup[1] = 42


edit_chai(chai)
print(chai)


def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)


make_chai("darjeeling", "Yes", "Low")  # postional
make_chai(tea="green", sugar="low", milk="no")  # keywords


def special_chai(*ingredients, **extras):
    print("ingredients", ingredients)
    print("extras", extras)


special_chai("cinnamon", "cardmom", sweetner="honey", foam="yes")

def chai_order(order=[]):
    order.append("masala")
    print(order)
    
    
chai_order()
chai_order()