import functools
vals = [2,4,6,8]
sum = functools.reduce(lambda x,y:x+y,vals)
print(sum)

char = ["w","o","r","l","d"]
word = functools.reduce(lambda x,y:x+y,char)
print(word)