def pour_chai(n):
    if n == 0:
        return "All cups Poured"
    return pour_chai(n - 1)


print(pour_chai(3))

chai_type = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai != "kadak", chai_type))
print(strong_chai)