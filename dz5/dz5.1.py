import random

def mixer(input_list: list) -> list:
    mixer = input_list[:]
    random.shuffle(mixer)
    return mixer

reference = ["олух", "пузырь", "остаток", "уловка"]
mixref = mixer(reference)
print("Мой список:", reference)
print("Перемешанный список:", mixref)
