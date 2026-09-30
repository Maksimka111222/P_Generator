import random
import string

def generate_base_password(length=8):
    characters = string.ascii_letters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("--- Базовий генератор паролів ---")
    try:
        user_length = int(input("Введіть довжину пароля (наприклад, 8): "))
        if user_length > 0:
            print(f"Ваш пароль: {generate_base_password(user_length)}")
        else:
            print("Довжина має бути більшою за нуль!")
    except ValueError:
        print("Помилка: введіть ціле число.")