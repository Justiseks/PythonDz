def fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

t = 10
fibl = list(fib(t))
print("Первые", t, "чисел Фибоначчи:", fibl)
