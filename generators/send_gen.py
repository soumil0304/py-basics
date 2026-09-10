def chai_cutomer():
    print("welcome! What Chai would you like ?")
    order = yield

    while True:
        print(f"preparing your {order}")
        order = yield


stall = chai_cutomer()
next(stall)  # start the generator
stall.send("masala chai")
