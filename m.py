import time
import multiprocessing

square_result = []

def calc_square(numbers):
    global square_result
    for n in numbers:
        time.sleep(5)
        print('square' + str(n*n))
        square_result.append(n*n)



if __name__ == "__main__":
    arr = [2,3,4,5,6]

    p1 = multiprocessing.Process(target = calc_square,args = (arr,))
    p1.start()
    p1.join()

    print('result'+ str(square_result))
    print("done!")




