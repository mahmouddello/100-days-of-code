import pandas as pd

students_dict = {
    "students": ["Mahmoud", "Anas", "Harry"],
    "scores": [90, 99, 78]
}

for key in students_dict:
    print(f"{key} : {students_dict[key]}")

# OR

for key, value in students_dict.items():
    print(f"{key} : {value}")
print("-" * 25)

# We can loop through using the same way above.

df = pd.DataFrame(students_dict)

for key, value in df.items():
    print(value)
print("-" * 25)
# But this is looping over columns only. Pandas provide a loop function to loop over rows:
# iterrows(): Pandas built-in function allows us to iterate over the rows of the dataframe

for index, row in df.iterrows():
    print(row.students)  # or we can print the scores of students
    print(row.values)  # or we can print the values of the dataframe

