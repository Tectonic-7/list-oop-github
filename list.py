students = ["kaisamba", "Foday", "Sharon"]
print(students)

#Accessing items in a list by their index
print(f"My bestfriends is {students[0]}")
print(f"My bestfriends is {students[1]}")
print(f"My bestfriends is {students[2]}")

# Get the index of an intem in a list using index
print(students.index("kaisamba"))
print(students.index("Sharon"))

#Know the number of items in a list using len
print(f"The total items in the list is: {len(students)}")

# Add items in a list using +=
students.append("Isatu")
print(students)
students += ["Kadiatu", "John", "Bintu"]

print(students)

#how to insert data in between a list using insert
students.insert(4, "Donald")
print(students)

#how to extend a list using extend
fruits = ["Apple", "Banana", "Mango"]
students.extend(fruits)
print(students)

#how to remove from a list using remove
fruits.remove("Mango")
print(fruits)

#how to remove the last element of a list using pop 
students.pop()
print(students)

thirdItem = students.pop()
print(thirdItem)