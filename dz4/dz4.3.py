def write(text, name):
    with open(name, mode='a+') as file:
        file.write(text + '\n')
    with open(name, mode='r') as file:
        linep = file.readlines()
        print("Информация из четных строк файла:")
        for index in range(1, len(linep), 2):
            print(linep[index].strip())

textp = "Первая строка\nВторая строка\nТретья строка\nЧетвертая строка\n"
name = "testdz.txt"

write(textp, name)