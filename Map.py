#map
def multiplication(n):
    return n * n

numbers = (1,2,3,4,5)
result = map(multiplication, numbers)
print(list(result))

#map with lambda
def multiplication(a):
    return a + a
result = map(lambda x: x + x , numbers)
print(list(result))


number1 = (5,7,8,9,10)
number2 = (7,8,9,18,11)
result = map(lambda x,y:x+y ,number1,number2)
print(list(result))


def double_even(num):
    if num % 2 ==0:
        return num*2
    else:
        return num
number = [1,7,8,9]
result = list(map(double_even ,number))
print(result)




