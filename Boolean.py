print(10>9)
print(10==9)
print(10<9)
#Using if else statement
a=200
b=30
if b>a:
    print("b is greater")
else:
    print("b is not greater")
#evaluating a string of a number
print(bool("hello"))
print(bool(15))

#evaluating two variables
x="hello"
y=15
print(bool("hello"))
print(bool(15))
#values that will return false
print(bool(False))
print(bool(0))
print(bool(None))
print(bool(""))
print(bool([]))
print(bool({}))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#creating functions that return a boolean value
def myFunction():
    return True

print(myFunction()) #returns true
#Print "Yes!" if the function returns True, otherwise print "no":
def myFunction():
    return True

if myFunction():
    print("Yes!")
else:
    print("no")

#isinstance
n=1j
print(isinstance(n,int))  
print(isinstance(n,complex))
