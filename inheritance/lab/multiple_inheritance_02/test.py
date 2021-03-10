from multiple_inheritance_02.teacher import Teacher
# from project.person import Person
# from project.employee import Employee

gosho = Teacher()
print(Teacher.__mro__)
print(gosho.sleep())
print(gosho.get_fired())
print(gosho.teach())