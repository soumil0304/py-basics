import threading 
import time 

def brew_chai():
    print(f"{threading.current_thread().name} started brewing process....")
    count = 0
    for _ in range(100_000_000):
        count+=1
    print(f"{threading.current_thread().name} finished brewing ")
    
thread1 = threading.Thread(target = brew_chai, name = "barista-1")
thread2 = threading.Thread(target = brew_chai, name = "barista-2")

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()

end = time.time()

print(f"total time taken : {end - start:.2f} seconds")