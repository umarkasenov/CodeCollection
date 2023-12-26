import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHI JKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

all = lower + upper + numbers
length = 8
password = "".join(random.sample(all, length))
name = (input("Введите названия!"))
with open("pasword.txt",  "a", encoding="utf-8") as file:
            file.write(f"{name}: {password}")