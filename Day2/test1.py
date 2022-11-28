#from test2 import employee
#this way we can import only particular class from an module(file) in the same package(directory)
import utils.util1
from utils.util1 import person2
#this way we are importing person2 class from util1 module(file) from the utils package(directory)

obj = person2("sunil", "maharana", 1996)
print(obj._n)
print(obj._person2__s)
print(obj.y)

class Person1:

    def __init__(self, name, surname, yob):

        self._n1 = name #_n means it is protected
        self.__s1 = surname #__s means it is private
        self.y1 = yob #no underscore means it is public
        #notations are used to declare public, private and protected variable

sunil = Person1(("ravi", "sunil"), ["maharana", "kumar"], {1,2,3})

print(sunil._n1) #we can call public and protected in this manner
print(sunil._Person1__s1) #we need to addres _classname before private variable to call it
print(sunil.y1)

