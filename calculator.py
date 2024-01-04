# import pygame
#
# WIDTH = 600
# HEIGHT = 800
#
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Umar")
#
# while True:
#     a = int(input("Введите число"))
#     b = input("Введте +, -, *, /,")
#     c = int(input("Введите число"))
#
#     if b == "+":
#       print(a + c)
#
#     elif b == "-":
#         print(a - c)
#
#     elif b == "*":
#         print(a * c)
#
#     elif b == "/":
#         print(a / c)
#
#     elif b == "//":
#         print(a // c)
#
#     elif b == "**":
#         print(a ** c)
#
import tkinter as tk
import ast


def on_button_click(value):
    current_text = entry.get()

    if value in ['+', '-', '*', '/']:
        entry.insert(tk.END, ' ' + value + ' ')
    else:
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text + str(value))


def clear_entry():
    entry.delete(0, tk.END)


def delete_last():
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text[:-1])


def calculate_result():
    try:
        expression = entry.get()
        # Используем ast.literal_eval для безопасного выполнения математических выражений
        result = ast.literal_eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Ошибка")


# Создание главного окна
root = tk.Tk()
root.title("Калькулятор")

# Виджет для ввода
entry = tk.Entry(root, width=16, font=('Arial', 24), justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4)

# Кнопки
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('Del', 5, 0)
]

for (text, row, col) in buttons:
    if text == 'Del':
        button = tk.Button(root, text=text, font=('Arial', 18), width=4, height=2, command=delete_last)
    else:
        button = tk.Button(root, text=text, font=('Arial', 18), width=4, height=2,
                           command=lambda t=text: on_button_click(t))

    button.grid(row=row, column=col, padx=5, pady=5)

# Запуск цикла обработки событий
root.mainloop()

