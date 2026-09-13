import threading
import time

def boil_milk():
    print(f"Boiling milk...")
    time.sleep(2)
    print(f"milk boiled")
    
def toast_bun():
    print(f"toasting bun ...")
    time.sleep(2)
    print(f"done toasting bun")
    
start = time.time()
t1 = threading.Thread(target = boil_milk)
t2 = threading.Thread(target = toast_bun)

t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()
print(f"Breakfast is ready ! is {end - start:.2f} seconds")