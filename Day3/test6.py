class ineuron:
    def students(self):
        print("Print Student Details")

class class_type():
    def students(self):
        print("Print the class type of students")

def ineuron_external(a):
    a.students()

i = ineuron()
j = class_type()

ineuron_external(i)
ineuron_external(j)

#function is same but by chaning the input, it is giving different output.
#ineuron_external(a) is behaving as a bridge between all the classes

#def test(a,b):
 #   return a+b
#print(test(3,4)) --> this is give a sum of the integers as 7
#print(test("sunil", " maharana")) --> this will give a concatination of strings
#hence, even the function is same it is giving different output depennding upon the input.

#here test() function is behaving differently for different inputs.
#When the input is integers, it is adding while when it is string it is concatinating.
#This is called Polymorphism.

#class
#object
#constructor
#public
#protected
#private
#modules
#package
#inheritance
#abstraction
#encapsulations
#polymorphism
#method overriding

#For all the classes that we have discussed in our class, point by point, write 10 examples
#Make sure to use ineuron, students, class, class type, number of courses, affiliates, blog, internship, jobs as a reference example
