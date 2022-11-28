class Person:

    def __init__(self, name, surname, yob):
        self._name = name
        self.__surname = surname
        self.yob = yob

sunil = Person("sunil", "maharana", 1996)

print(sunil._name)
print(sunil._Person__surname)
