myList = ("Apples","bananas","oranges")
myIt = iter(myList)

print(next(myIt))
print(next(myIt))
print(next(myIt))

#iterable strings
myStr = "mathematics"
mySub = iter(myStr)

print(next(mySub))
print(next(mySub))
print(next(mySub))
print(next(mySub))
print(next(mySub))
print(next(mySub))
print(next(mySub))
print(next(mySub))
print(next(mySub))
print(next(mySub))
print(next(mySub))

#looping through an iterator

myList = ("Apples","bananas","oranges")
for x in myList :
    print(x)
    
myStr = "mathematics"
for x in myStr :
    print(x)
    
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
