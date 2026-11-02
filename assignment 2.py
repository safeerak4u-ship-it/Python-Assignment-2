
# Que 1: List Creation

# a. Create age_list with five integer elements
age_list = [24, 25, 26, 27, 28]

# b. Create name_list with five string elements
name_list = ["Hezi", "Sara", "Zara", "Yami", "Maya"]

print("Age List:", age_list)
print("Name List:", name_list)


# Que 2: List Operations / Modifications

# a. Append Yazhini to name_list
name_list.append("Yazhini")
print("After append:", name_list)

# b. Insert 30 at index 2 in age_list
age_list.insert(2, 30)
print("After insert:", age_list)

# c. Remove Yazhini from name_list
name_list.remove("Yazhini")
print("After remove:", name_list)

# d. Pop the last element from age_list
age_list.pop()
print("After pop:", age_list)

# e. Extend age_list with additional ages
age_list.extend([29, 30, 26])
print("After extend:", age_list)

# f. Sort age_list in descending order
age_list.sort(reverse=True)
print("Descending order:", age_list)

# g. Find maximum, minimum and sum
print("Maximum age:", max(age_list))
print("Minimum age:", min(age_list))
print("Sum of ages:", sum(age_list))


# Que 3: Accessing List Elements

# a. Print the first element
print("First element:", name_list[0])

# b. Print the last element
print("Last element:", name_list[-1])

# c. Print elements from index 2 to index 4
print("Elements from index 2 to 4:", name_list[2:5])

# d. Print elements in reverse order
print("Reverse order:", name_list[::-1])


# Que 4: Dictionary

# a. Create a dictionary with five students and their marks
student_marks = {
    "Hezi": 75,
    "Sara": 78,
    "Zara": 90,
    "Yami": 85,
    "Maya": 88
}

print("Student Marks:", student_marks)

# b. Access and print the mark of a specific student
print("Yami's Marks:", student_marks["Yami"])

# c. Add a new student Janani with 80 marks
student_marks["Janani"] = 80
print("After adding Janani:", student_marks)

# d. Update an older student's mark to 82
student_marks["Sara"] = 82
print("After updating Sara's marks:", student_marks)

# e. Print keys, values and items
print("Student Names:", student_marks.keys())
print("Student Marks:", student_marks.values())
print("Student Details:", student_marks.items())


# Que 5: Sets

# a. Create a set with the given values
my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}

print("My Set:", my_set)

# b. Attempt to change an element in the set
try:
    my_set[4] = 's'
except TypeError as error:
    print("Error:", error)
    print("Explanation: Sets do not support indexing or item assignment.")

# c. Create two sets
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

# d. Calculate union and intersection
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))


# Que 6: Performance Category Program

score = int(input("Enter your score (0 to 10): "))

if score < 0 or score > 10:
    print("Invalid score! Please enter a score between 0 and 10.")

elif score > 7:
    print("Above Average: Excellent work! Keep it up!")

elif score >= 4:
    print("Average: Good effort! Keep practicing, there's room for improvement.")

else:
    print("Below Average: Need to improve your performance. Consistent practice will lead to better results.")
