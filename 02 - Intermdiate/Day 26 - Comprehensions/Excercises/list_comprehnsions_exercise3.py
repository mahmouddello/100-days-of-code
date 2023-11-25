# Common numbers between two lists

with open("../file1.txt", mode='r') as file1:
    numbers_1 = file1.readlines()
    numbers_1 = [int(number) for number in numbers_1]
    print(numbers_1)

with open("../file2.txt", mode='r') as file2:
    numbers_2 = file2.readlines()
    numbers_2 = [int(number) for number in numbers_2]
    print(numbers_2)

result = [number for number in numbers_1 if number in numbers_2]
print(result)

print("-" * 25)
