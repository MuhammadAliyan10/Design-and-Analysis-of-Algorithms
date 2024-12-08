

def fibonacci(num):
    a,b = 0, 1
    sequence = []
    for _ in range(num):
        sequence.append(a)
        a, b = b , a + b
    return sequence



print(fibonacci(10)) 
