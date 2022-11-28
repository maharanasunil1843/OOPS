class ineuron:
    __students = "data science" #private variable

    def student(self):
        print(ineuron.__students)

i = ineuron()
i.student()
print(i._ineuron__students)

#Here, we are trying to hide "data science" behind class "ineuron". This is called data abstraction
#If we are not giving direct access of dataset to a user, it is called data abstraction
