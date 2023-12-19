import random
import string

def generate_password(length=8):
    characters = string.digits  # Только цифры
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def write_to_file(password, name):
    try:
        with open('passwords.txt', 'a') as file:
            file.write(f"{name}: {password}\n")
        print(f"Пароль успешно записан в файл 'passwords.txt'")
    except Exception as e:
        print(f"Произошла ошибка при записи в файл: {e}")

# Запрашиваем у пользователя название для пароля
password_name = input("Введите название для пароля: ")

# Генерируем пароль длиной 12 цифр и записываем его в файл
generated_password = generate_password(12)
write_to_file(generated_password, password_name)
