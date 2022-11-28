class Person:

    def age(self, current_year, year_of_birth):
        return current_year - year_of_birth

    def email_id_input(self, emailid):
        print("takes an email id from an person and prints it", emailid)

    def ask_name(self):
        name = input("Enter your name")
        return name

    def ask_dob(self):
        dob = input("Enter your Date of Birth")
        return dob

sunil = Person()
ravi = Person()
ashok = Person()
abhishek = Person()

print(sunil.age(2022, 1995))
#class variable has been created, it is not asking for any input value because we have not used constructor __init__ method

sunil.email_id_input("sunil@gmail.com")
print(sunil.ask_name())

print(ravi.ask_dob())