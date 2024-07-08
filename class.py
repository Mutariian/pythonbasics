class myclass:
    x=5
p1=myclass
print(p1.x)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1 = person("Ian",20)
print(p1.name,p1.age)

#The string representation of an object WITHOUT the __str__() function
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1 = person("Ian",20)
print(p1)

#The string representation of an object WITH the __str__() function

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name} {self.age}"

p1=person("Ian",20)
print(p1)

#object method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Ian Mutari", 21)
p1.myfunc() 
p1.age=30
print(p1.age)
