import threading
import time


def cal_square(numbers):
    print("calculate square of numbers")
    for n in numbers:
        time.sleep(0.1)
        print('square:',n*n)
        
def cal_cube(numbers):
    print("calculate the cube of the numbers")
    for n in numbers:
        time.sleep(0.1)
        print('cube:',n*n*n)

arr = [2,3,4,5,6]

time.time()
t1 = threading.Thread(target=cal_square,args=(arr,))
t2 = threading.Thread(target=cal_cube,args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()


print("done in :",time.time())
print("hey i did done this calculation")
print("bye")