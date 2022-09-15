from threading import *
import time
def display():
    for i in range(10):
        print("Seetha Thread")
        time.sleep(2)
t=Thread(target=display)
t.start()
t.join(5)        #This Line executed by Main Thread
for i in range(10):
    print(i)
