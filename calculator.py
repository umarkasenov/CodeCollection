import random

knb = ['камень', 'ножницы', 'бумага']

user = input('введите камень ножницы бумага')

bot = random.choice(knb)
while True:
    if bot == user:
        print("ничья")
    elif (bot == 'камень' and user == 'ножницы' or
          bot == 'ножницы' and user == 'бумага' or
          bot == "бумага" and user == "камень"):
        print(f'бот выбрал {bot} я выбрал {user} бот выйграл')

    elif (user == 'камень' and bot == 'ножницы' or
          user == 'ножницы' and bot == 'бумага' or
          user == "бумага" and bot == "камень"):
        print(f'я выбрал {bot} я выбрала {user} я выйграл')

    else:
        print("Неправильный ввод")




while True:
    color = input("Введите цвет")
    if color == 'красный':
        print('остановись')

    elif color == 'желтый':
        print('приготовся')

    elif color == 'зеленный':
        print('поехали')
    else:
        print('неправильный ввод')
