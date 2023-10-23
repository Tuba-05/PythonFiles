# t=eval(input('enter values:'))
# print('t=',t)
# l=list(t)
# print('l=',l)
# l.reverse()
# t=tuple(l)
# print('t=',t)
#
#
# T=[(1,2,3,),(5,7,9),('a','b','c')]
# print(T)
#
# print('T=',[i[:2] for i in T])
#
# r1=int(input('enter first range values:?'))
# r2=int(input('enter second range values:?'))
# num= r1 + 1
# count = 0
# while num < r2:
#     res = num % 2
#     if ( num % 2 ) > 0:
#         count+=1
#     num+=1
# print('odd count:%d'%(count))
# class Parent:
#     def __init__(self):
#         self.value = 5
#
#     def get_value(self):
#         return self.value
#
#
# class Child(Parent):
#     def get_value(self):
#         return self.value + 1
#
#
# billy = Child()
# print(billy.get_value())


class Parent:
    def __init__(self, name, eye_colour):
        self.name = name
        self.eye_colour = eye_colour

    def properties(self):
        return f"{self.name}'s eye colour is {self.eye_colour}"


class Child:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def properties(self, x):
        return f"{self.name}'s eye colour is also {x} "


Person = Parent("Bob", "Green")
Kid = Child("Billy", 14)

print(Person.properties())
print(Kid.properties(Person.eye_colour))
