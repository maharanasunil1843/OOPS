#classes: Classification of real world entity or moudles.
#objects: objects represetns a real entity/data/function.

class Person :

    def __init__(sunil, name, surnane, emailid, year_of_birth):
        #__init__ is an inbuilt method a.k.a. constructor
        #self is not a reserved keyword, it can be anything. As it is the first variable, it will be treated as pointer.

        sunil.n = name #Here name on the right side is should be same as mentioned in the class
        #but name on the left can be anything, it is just used as a pointer to assign data to the class

        sunil.s = surnane
        sunil.e = emailid
        sunil.y = year_of_birth

    def __init__(sunil, name, surname):
        sunil.n = name
        sunil.s = surname
        #Hence, while executing this code, an error will be given that Person.__init__() take only 3 arguements including pointer.
        #it simply means that it is only considering the latest __init__ function.

    def age(sunil, current_year_birth):
        return current_year_birth - sunil.y


anuj_var = Person("anuj", "bhandari", "anuj@gmail.com", 1994)
#anuj_var is an object of class Person.
#data flow: "sunil" passed in anuj_var --> name in __init__ --> pointer.var for name --> pointer.var points the data to Person class
sunil = Person("Sunil", "Maharana", "sunil@gmail.com", 1996)
ravi = Person("Ravi", "Garg", "ravi@gmail.com", 1990)


print(anuj_var.n)
#here we are accessing the data of the anuj_var by putting the suffix .var for the name of __init__
#Example to explain the data in test1.py
print(sunil.s)
print(ravi.y)
print(anuj_var.n + " " + anuj_var.s)
print(type(sunil))

#Age of a person class can be called using class variable aka object.function()
#Here we have given one arguemnt in age and second value is taken from __init__ using pointer
#So age of sunil can be called using following syntax

print(sunil.age(2022))