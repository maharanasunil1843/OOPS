class ineuron:
    def __init__(self):

        self.students1 = "data science"

    def students_fun(self):
        print(self.students1)

i = ineuron()
print(i.students1)
i.students_fun()
#i.students1() #Hence, calling string directly is not possible
i.students1 = "data analytics"
i.students_fun() #overriding the value in run time is possible because it is public variable.
print("\n")

class ineuron1:
    def __init__(self):

        self.__students1 = "data science1"

    def students_fun(self):
        print(self.__students1)

    def students_change(self, new_value): #this is called setter, as we are trying to set the value of the variable
        self.__students1 = new_value

i1 = ineuron1()
i1.students_fun()
i1.__students1 = "big data"
i1.students_fun() #Hence, it is not able to change the value of the private variable in real time using an object.
i1.students_change("Sunil Maharana")
i1.students_fun() #Hence, it is possible to change the value of the private variable by reassigning its value via a class-method
#this phenomenon is called Encapsulation.

#Concept of Encapsulation says that you are not supposed to allow the user to change the value of the variable directly.

