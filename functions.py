def my_function(fname):
    print(fname + "mutari")

my_function("ian ")
my_function("ivy ")
my_function("allan ")
my_function("nick ")

def my_name(fname,lname):        #function with two arguments
    print(fname + " " + lname)
my_name("Ian","Mutari")

def my_function(*kids):
    print("The smallest kid is " + kids[2])
my_function("Allan ","Ivy ","Ian","Nick")

def my_function(kid1,kid2,kid3,kid4):
    print("The youngest kid is "+kid3)
my_function(kid4="Nick",kid2="Ivy",kid3="Allan",kid1="Ian")

def my_name(**name):
    print("my name is "+name["lname"])
my_name(fname="Ian",lname="Kiplagat")

#default parameter value
def my_function(country="Kenya"):
    print("Iam from "+country)

my_function("Uganda")
my_function("Tanzania")
my_function()        #calling an arg without a default value
my_function("Canada")

#Passing a list in an argument
def my_function(fruits):
    for x in fruits:
        print(x)

fruits=["mangos","Oranges","bananas","lemon"]

my_function(fruits)

#return values
def my_function(x):
    return x * 5

print(my_function(3))
print(my_function(5))
print(my_function(8))

#positional-only argument
def my_function(x,/):
    print(x)

my_function(247)

def my_function(x):
    print(x)

my_function(x=101776)


#keyboard only argument
def my_function(*,x):
    print(x)
my_function(x=2)

def my_function(x):
    print(x)
my_function(2)

#positional only and keyboard only
def my_function(a,b,c,/,*,d):
    print(a+b+c+d)

my_function(3,4,5,d=6)

#Recursion
def tri_recursion(k):
    if(k>0):
        result= k + tri_recursion(k-1)
        print(result)
        return result
    else:
        result=0
        return result
print("\n\nRecursion Example Results ")
tri_recursion(6)





