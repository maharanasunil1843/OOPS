class ineuron: #parent class
    def student(self):
        print("Print the details of all the student")

    def achievers(self):
        print("Print the list of all the achievers")

    def hall_of_fame(self):
        print("Print everyone from hall of fame")

class ineuron_vision(ineuron): #child class
    def student(self):
        print("These are the filtered student lists.")

iv = ineuron_vision()
i = ineuron()
iv.student() #it is calling student from ineuron_vision class. It is called method overriding.
i.student()
