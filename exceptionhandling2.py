a = 5
b = 7
k = int(input("Enter any number"))
print(k)

try:
    print("resource open")
    print(a/b)

except ValueError  as e:
    print("Hey,you cannot enter any Letters")


except ZeroDivisionError  as e:
    print("Hey,you cannot divide a Number by Zero",e)

