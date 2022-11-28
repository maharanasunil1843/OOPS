import test1 as t

obj3 = t.Person1("sunil", "maharana", 1996)
print(obj3._n1)
print(obj3._Person1__s1)
print(obj3.y1)

#Hence, we can access private and protected variables also across python unlike javascript, scala or anyother language


class person:

    _name = "sunil" #protected
    __surname = "maharana" #private
    yob = 1996 #public
    #all the above variables are called global variables

    def _age(self, current_year): #protected function
        return current_year - self.yob

    def __age1(self, current_year): #private function
        return current_year - self.yob


obj = person()
print(obj._age(2022))
print(obj._person__age1(2022))




class employee(person):
    #inheritance: employee class is inheriting all the methods along with variables of class person.
    #Here person class is called parent class and employee class is called child class
    _name = "badrinath"
    __surname = "kumar"
    yob = 2000
    #by declaring new values in the class, it will over write the inheritance and assign new values to the variable

obj1 = employee()
print(obj1)
print(obj1._age(2022))
print(obj1._person__age1(2022)) #Here the age will be different because self.yob is different in employee class
print(obj1.yob) #We have declared yob in person class but calling it inside employee class because of inheritance
print(obj1._name)
print(obj1._person__surname)
print(obj1._employee__surname)
#as yob is public, it is coming under suggestion but _name and __surname is not appearing because those are protected and private



