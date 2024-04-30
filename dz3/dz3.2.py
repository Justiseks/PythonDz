def allp(listp : list, multip: float | int = 2) -> list:
    listp2= []
    for x in listp:
        x *= multip
        listp2.append(x)
    return listp2

print("Список:\n[8, 7, 4]")
print("Список элементов, умноженный на 2 через функцию:")
print(allp([8, 7, 4], 2))

alllamp = lambda listp, multip = 2: [x * multip for x in listp]

print("Список элементов, умноженный на 2 через лямбда функцию:")
print(alllamp([8, 7, 4], 2))