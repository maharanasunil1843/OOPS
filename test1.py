#classes: Classification of real world entity or moudles.
#objects: objects represetns a real entity/data/function.

class Person :

    def __init__(self, name, surnane, emailid, year_of_birth):
        #__init__ is an inbuilt method a.k.a. constructor
        #self is not a reserved keyword, it can be anything. As it is the first variable, it will be treated as pointer.

        self.name = name #Here name on the right side is should be same as mentioned in the class
        #but name on the left can be anything, it is just used as a pointer to assign data to the class

        self.surname = surnane
        self.emailid = emailid
        self.year_of_birth = year_of_birth

anuj_var = Person("anuj", "bhandari", "anuj@gmail.com", 1994)
#anuj_var is an object of class Person.
#data flow: "sunil" passed in anuj_var --> name in __init__ --> pointer.var for name --> pointer.var points the data to Person class
sunil = Person("Sunil", "Maharana", "sunil@gmail.com", 1996)
ravi = Person("Ravi", "Garg", "ravi@gmail.com", 1990)


print(anuj_var.name)
#here we are accessing the data of the anuj_var by putting the suffix .var for the name of __init__
#all these examples are mentioned in the test2.py file in this same directory
print(sunil.surname)
print(ravi.surname)
print(anuj_var.name + " " + anuj_var.surname)
print(type(sunil))