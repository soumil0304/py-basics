def serve_chai():
    yield "Cup 1 : Masala Chai"
    yield "Cup 2 : ginger Chai"
    yield "Cup 3 : Elaichi Chai"


stall = serve_chai()

# for cup in stall
# print (cup)

def get_chai_list():
    return ["cup 1", "cup 2", "cup 3"]


# generator function
def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"


chai = get_chai_gen()
print(next (chai))
print(next (chai))
print(next (chai))
#print(next (chai))  #gives error