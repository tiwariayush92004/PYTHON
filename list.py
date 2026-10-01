# lists are mutable**************

marks = [99,98,87,57,46,55,33,27,66,87,72]

# lenth of the list 
print(len(marks))

# slicing
print(marks[0:3]) #last index is not included it will go till 0-2

# adding new value to last
marks.append(60)
print(marks)

# inserting at any particular index 
marks.insert(3,122) #it will intert value 122 to index 3 (index,value)
print(marks)