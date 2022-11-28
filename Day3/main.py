class car : #parent class

    def __init__(self, body, engine, tyre):

        self.b = body
        self.e = engine
        self.t = tyre

    def milage(self):

        print("milage of this car ")

class tata(car): #child class
    pass

c = car("solid", "V6", "radial")
t = tata("solid", "V8", "radial")

print(c)
print(t)

print(t.milage())