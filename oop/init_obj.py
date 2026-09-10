class chaiorder:

    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size} ml of {self.type} chai"

order = chaiorder("Masala", 200)
print(order.summary())

order2 = chaiorder("ginger", 220)
print(order2.summary())
