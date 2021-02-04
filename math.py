def subtract(a,b):
    if a<b:
        return "Error: Negative value"
    return a-b

def divide(a,b):
    if b==0:
        return "Exception: Division by zero"
    return a/b

def square(a):
    if a<=0:
        return "Error: Only positive numbers allowed"
    return a*a
    