class Parent1:
    value1="this is value 1"
    value2="this is value 2"
class Parent2:
    value1="this is value 1"
    value2="this is value 2"
class Child(Parent1,Parent2):
    pass

parent_1=Parent1()
print(parent_1.value1)
print(parent_1.value2)
child_1=Child()
print(child_1.value1)
print(child_1.value2)
