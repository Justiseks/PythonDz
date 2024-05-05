def decorator(func):
    def abcp(*args, **kwargs):
        comma = ', '.join(map(str, args))
        print(f"Функция {func.__name__} была вызвана с позиционными аргументами: ({comma}) и именованными аргументами: {kwargs}")
        return func(*args, **kwargs)
    return abcp

@decorator
def fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

t = 10
fibl = list(fib(t))
print("Первые", t, "чисел Фибоначчи:", fibl)
