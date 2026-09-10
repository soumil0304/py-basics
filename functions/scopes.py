def serve_chai():
    chai_type = "masala chai"
    print(f"inside function {chai_type}")


chai_type = "lemon"
serve_chai()
print(f"outside function {chai_type}")


def chai_counter():
    chai_order = "lemon"  # enclosing

    def print_order():
        chai_order = "ginger"
        print("inner :", chai_order)

    print_order()
    print("outer :", chai_order)


chai_order = "tulsi"
chai_counter()
print("global:", chai_order)
