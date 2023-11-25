fruits = ["Apple", "Pear", "Orange"]


# Catch the exception
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(f"{fruit} pie")


make_pie(4)
