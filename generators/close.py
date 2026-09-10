def local_chai():
    yield "masala chai"
    yield "ginger chai"


def imported_chai():
    yield "matcha"
    yield "oolong"


def full_menu():
    yield from local_chai()
    yield from imported_chai()


for chai in full_menu():
    print(chai)


def chai_stall():
    try:
        while True:
            yield "waiting for chai order"
    except:
        print("stall is closed ")


stall = chai_stall()
print(next(stall))
stall.close()  # cleanup 

