def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return None
a=int(input('Enter a number: '))
b=int(input('Enter another number: '))
print(divide(a, b))