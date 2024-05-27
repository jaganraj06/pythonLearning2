#zip
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]
mydict = {k:v for (k,v) in zip(keys,values)}
print(mydict)

place = ('tiruchi','chennai','selam')
project = ('Tidalpark','Metro','Tidalpark')
price = ('60000000000','700000000000','60000000000')
zipped = list(zip(place,project,price))
print(zipped)
