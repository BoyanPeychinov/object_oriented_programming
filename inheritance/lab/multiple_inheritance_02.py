class Person:
    def sleep(self):
        return "sleeping..."


class Employee:
    def get_fired(self):
        return "fired..."


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."


gosho = Teacher()
print(Teacher.__mro__)
print(gosho.sleep())
print(gosho.get_fired())
print(gosho.teach())