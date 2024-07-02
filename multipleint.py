class Father ():
    def skills (self):
        print(" singing ", " writeing ")

class Mother ():

    def skills(self):
        print(" programing "," gardening ")

class child (Father,Mother):
    def skills(self):
        Father.skills()
        Mother.skills()
         print("sports")

c=child()
child.skills()




