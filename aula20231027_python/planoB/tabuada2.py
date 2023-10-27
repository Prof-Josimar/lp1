import time
import os

os.system("cls")
for i in range(10):
    os.system("cls")
    print("Tabuada de ", (i + 1))
    for j in range(10):
        print("{:2} x {:2} = {:2}".format((i + 1), j, (i * j)))
    print("_" * 20)
    time.sleep(1)
