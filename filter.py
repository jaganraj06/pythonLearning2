#filter
items=[(2334,"phone",89),(4555,"car",90),(2345,"bike",78),(7890,"house",97)]
less_then_500 = lambda item:item[2]<500
filtered = list(filter(less_then_500,items))
print(filtered)
filtered = list(filter(lambda item:item[1][0]=='p',items))
print(filtered)
filtered = list(filter(lambda item:item[1][0]=='h',items ))
print(filtered)