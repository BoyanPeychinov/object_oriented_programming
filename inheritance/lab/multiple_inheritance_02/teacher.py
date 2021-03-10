from multiple_inheritance_02.person import Person
from multiple_inheritance_02.employee import Employee


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."