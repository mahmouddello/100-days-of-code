from art import logo


# Adding function
def add(a, b):
    return a + b


# Substracting function
def substract(a, b):
    return a - b


# Multiply function
def multiply(a, b):
    return a * b


# Divide function
def divide(a, b):
    return a / b


# Creating a dictionary to save mathematical operations
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide

}


def calculator():
    print(logo)
    number1 = float(input("Entre first number: "))
    should_continue = True
    """علم او فلاغ للتحكم بايقاف الوايل لووب"""
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")
        """اختيار رمز عملية سواء كان جمع ام طرح الخ..."""
        number2 = float(input("Entre second number: "))
        calculation_function = operations[operation_symbol]
        """الحصول على اسم الفنكشن(القيمة للمفتاح) عن طريق المفتاح من القاموس"""
        answer = calculation_function(number1, number2)
        print(f"{number1} {operation_symbol} {number2} = {answer}")
        if (input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation")) == 'y':
            should_continue = False
            number1 = answer
        else:
            # Recursion
            calculator()


calculator()
