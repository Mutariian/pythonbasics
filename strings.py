a="niaje"
print(a)
b='''my name is ian,
iam a Telecommunication Engineering Student,
currently practicing python'''
print(b)
c="Hello,world!"
print(c[2])   #getting the character at position 2
#looping through a string
for x in "mutari":
    print(x)
#length of a string
print(len(c))
#cheking string
txt="My name is Engineer Mutari"
print("Engineer"in txt)
#using if statement in cheking string
if 'Engineer'in txt:
    print("Yes,'Engineer'is present")
#checking if NOT
print("doctor"in txt)
if 'doctor'not in txt:
    print("No.'doctor'is not present")
    
#F string
Age = 21
txt=F"my name is Ian ,iam {Age} years old"
print(txt)
#placeholder and modifiers
price=35
Txt=f"the product is {price:.2f}"
print(Txt)
text=f"the price of the product is {20 * 35}"
print(text)