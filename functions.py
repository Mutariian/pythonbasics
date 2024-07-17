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

def greet():
    print("Hello there")
    print("How are you doing")

greet()

def greet(fname,lname):
    print(f"Hi {fname} {lname}")
    print("Welcome aboard")


greet("Ian","Mutari")
greet("Allan","Mutari")

def sum(a,b):
    total=a+b
    return total

n=sum(12,14)
print("total =",n)
m=sum(12,19)
print("total =",m)

def function1(x):
    return 2**x

a=function1(3)
print("value =",a)
b=function1(4)
print("value =",b)

def calculate_total(exp):          #function argument(input)
    total=0
    for item in exp :
        total=total+item
    return total                    #return value(output)

Kiplagat_exp=[12,123,678]
Ian_exp=[90,30,128]

Kiplagat_total=calculate_total(Kiplagat_exp)
Ian_total=calculate_total(Ian_exp)

print("KIplagat's total expenses is ",Kiplagat_total)
print("Ian's total expenses is ",Ian_total)

#bmi calculator
name1="Alvin "
height_m1=2
weight_kg1=90

name2="Marion "
height_m2=1.80
weight_kg2=80

name3="Rachel "
height_m3=1.60
weight_kg3=70

def bmi_calculator(name,height_m,weight_kg):
    bmi=weight_kg/(height_m**2)
    print ("bmi: ")
    print(bmi)
    if bmi<25 :
        return name + "is not overweight"
    else:
        return name + "is overweight"

result1=bmi_calculator(name1,height_m1,weight_kg1)
result2=bmi_calculator(name2,height_m2,weight_kg2)
result3=bmi_calculator(name3,height_m3,weight_kg3)

print(result1)
print(result2)
print(result3)




