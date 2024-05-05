nump = [x ** 2 for x in range(1, 11)]

week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
weekdict = {day: index + 1 for index, day in enumerate(week)}

tagp = {"Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"}
tagplow = {tag.lower() for tag in tagp}

print("Список квадратов первых 10 натуральных чисел:", nump)
print("Словарь, содержащий названия дней недели и их порядковые номера:", weekdict)
print("Множество, содержащее теги библиотек в нижнем регистре:", tagplow)
