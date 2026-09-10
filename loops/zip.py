name = ["soumil", "dipanshu", "cherry", "hitesh"]
bill = [100, 200, 300, 400]

for name, amount in zip(name, bill):
    print(f"Hello {name}, your bill is ${amount}")