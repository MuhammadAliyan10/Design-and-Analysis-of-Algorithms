def GDC(a,b):
    while b != 0:
        a, b = b , a % b
    return a


num1 = 56
num2 = 98
result = GDC(num1, num2)
print(f"The GCD of {num1} and {num2} is {result}")