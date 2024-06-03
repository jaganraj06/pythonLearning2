a = 10
b = 11
a = a + 1

print(id(a))
print(id(a)==id(b))

class box:
    def __init__(self,l):
        self.len = l

b1 = box(5)
b2 = box(6)
print(b1.len)
print(b2.len)
