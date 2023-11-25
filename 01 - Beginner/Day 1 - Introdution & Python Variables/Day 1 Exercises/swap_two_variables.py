a = input("a : ")
b = input("b : ")
# swap a and b values by using a temporary variable
temp = a # storing a value in temp variable
a = b # storing b value in the variable a
b = temp # now storing the temp value in variable b which is previously old a value
print("a : "+a)
print("b : "+b)
