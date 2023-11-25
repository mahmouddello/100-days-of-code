# Classic Syntax
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    new_list.append(n + 1)

print(new_list)
# List Comprehensions: new_list2 = [new_item for item in list]

new_list2 = [n + 1 for n in numbers]
print(new_list2)
print("-" * 50)

# Example 2: String as a list
name = "Angela"
letters = [letter for letter in name]
print(letters)
print("-" * 50)
# Example 3: with conditions

names = ["Alex", "Ben", "Claudia", "Dave", "George", "Harry Kane"]

short_list = [short_name for short_name in names if len(short_name) < 5]
print(short_list)

uppercase_list = [name.upper() for name in names if len(name) > 5]
print(uppercase_list)
print("-" * 50)
