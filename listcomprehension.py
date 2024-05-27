sq_list = list(map(lambda x:x*x,range(1,11)))
print(sq_list)
sq_list = [x*x for x in range(1,11)]
print(sq_list)

temp = [10,20,30,40,50,60]
temp_filtered = [i for i in temp if i>30]
print(temp_filtered)
temp_filtered = [i if i<45 else 0 for i in temp]
print(temp_filtered)

#dictionarycomprehension
cart = {'phone':25000.8,'car':2200000,'house':6000000}
cart_rounded = {k:round(v) for(k,v) in cart.items()}
print(cart_rounded)# roundoff the val
cart2 = {k:v for (k,v) in cart.items() if v>100000}
print(cart2)

square_dict = dict()
for num in range(1,11):
    square_dict[num] = num*num
print(square_dict)








