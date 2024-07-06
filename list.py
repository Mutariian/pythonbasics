shopping=["maize floor","rice","sugar","coffee"]
print(shopping)
print(len(shopping))#determing how many items are in the list

marks=[80,70,90,89,96]
print(marks)

studentid=[15173,"Ian",True,'Engineer']
print(studentid)

print(type(marks))

#Accessing list items
print(shopping[0])    #the first item in the list
print(marks[2])
print(studentid[3])
print(shopping[-1])   #the last item in the list
print(marks[-2])      #the second last item in the list

#range of indexes
print(shopping[0:3])
print(marks[:3])
print(studentid[1:])
print(marks[-5:-1])  #starts from -5 but doesn't include -1

#checking if item exist 
groceries=["apple","bananas","tomatoes","mangoes"]
if "bananas" in groceries:
 print("Yes there is banana ")

 if "onions" not in groceries:
    print("Not in the groceries")

#changing items in a list
groceries[1]="machungwa"   #changing the second item in the groceries list
print(groceries)

groceries[1:3]="oranges","cherry" #changing the second and third item 
print(groceries)

groceries[1:2]="sukuma","cabbage" #replacing the second index with two variables
print(groceries)
print(len(groceries))

groceries[1:3]="garlic"
print(groceries)

#inserting items in a list
points=[10,20,20,40,50,60]
print(len(points))
points.insert(2,30)
print(points)
print(len(points))

#adding items to the end of the list
library=["books","jornals","magazines","research area"]
library.append("computers")
print(library)

#append elements from another list to the current list
library.append(points)
print(library)

library.extend(points)
print(library)

#removing items
courses=["TIE","EEE","IT","GEGIS"]
courses.remove("IT")
print(courses)

library=["books","jornals","magazines","research area"]
library.pop(1)  #removes the item in index 1
print(library)

library=["books","jornals","magazines","research area"]
library.pop()     #removes the last index
print(library)

library=["books","jornals","magazines","research area"]
del library[0]
print(library)

library=["books","jornals","magazines","research area"]
del library        #removes the entire list

library=["books","jornals","magazines","research area"]
library.clear
print(library)





