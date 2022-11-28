class Person:
    def __init__(self, name, surname, emailid, yob):
        self.name = name
        self.surname = surname
        self.emailid = emailid
        self.yob = yob

    def age(self, current_year):
        return current_year - self.yob

anuj_var = Person("anuj", "bhandari", "anuj@gmail.com", 1994)

print(anuj_var.name)
print(anuj_var.surname)
print(anuj_var.emailid)
print(anuj_var.yob)
print(type(anuj_var))
print(anuj_var.age(2022))



