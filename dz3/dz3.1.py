def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        raise ValueError("нельзя делить на ноль.")
    return x / y
def power(x, y):
    return x ** y

while 1:
    print("Что вы хотите сделать?")
    print("1 - сложение\n2 - вычитание\n3 - умножение\n4 - деление\n5 - возведение в степень\n6 - выход из программы")
    nump = input()

    if nump not in ['1', '2', '3', '4', '5', '6']:
        print("Такой функции нет.")
        continue

    if nump in ['1', '2', '3', '4', '5']:
        x = int(input("Введите первое число: "))
        y = int(input("Введите второе число: "))

    match nump:
        case '1':
            print(add(x, y))
        case '2':
            print(subtract(x, y))
        case '3':
            print(multiply(x, y))
        case '4':
            try:
                print(divide(x, y))
            except ValueError as e:
                print("Ошибка:", e)
                continue
        case '5':
            print(power(x, y))
        case '6':
            break
