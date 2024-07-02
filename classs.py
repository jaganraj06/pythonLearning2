#class Human:
    #def __init__(self,n,o):
        #self.name = n
        #self.occupation = o
    #def do_work(self):
        #if self.occupation == "tennis player":
            #print(self.name,"play tennis")
        #elif self.occupation == "actor":
            #print(self.name,"shoots flims")
    #def speaks(self):
        #print(self.name,"says how are you?")

#tom = Human("tom cruise","tennis player")
#tom.do_work()
#tom.speaks()

#maria = Human("mariaa","actor")
#maria.do_work()
#maria.speaks()


class vehicle:
    def general_usage(self):
        print("general use: transpotation")

class Car(vehicle):
    def __init__(self):
        print("I'm car")
        self.wheels = 4
        self.have_roof = True
    def specific_usage(self):
        print("specific use: commute to work, vacation with family")
class Motorcycle(vehicle):
    def __init__(self):
        print("I'm motorcycle")
        self.wheels = 2
        self.have_roof = False
    def specific_usage(self):
        print("specific use:commute to work, rideing in highway")

c = Car()
m = Motorcycle()
print(isinstance(c,Motorcycle))
print(issubclass(Car,vehicle))


