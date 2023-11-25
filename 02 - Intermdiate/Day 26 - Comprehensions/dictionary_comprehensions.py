import random

# Comprehensions Syntax:
# new_dict = {new_key: new_value for item in list}

# new_dict = {new_key: new_value for (key,value) in dict.items}

# Conditional Comprehensions Syntax:
# new_dict = {new_key: new_value for (key,value) in dict.items if test}

# Dictionary comprehension using a list
names = ["Alex", "Ben", "Claudia", "Dave", "George", "Harry Kane"]
students_scores = {student: random.randint(0, 100) for student in names}
print(students_scores)

# Conditional Dictionary comprehension using a dictionary
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)
