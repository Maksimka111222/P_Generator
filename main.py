import random
import string

def generate_base_password(length=8):
    characters = string.ascii_letters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_advanced_password(length=8, use_digits=True, use_specials=True):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation
        
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("--- Генератор паролів ---")
    try:
        user_length = int(input("Введіть довжину пароля (наприклад, 8): "))
        if user_length > 0:
            choice = input("Використовувати цифри та спецсимволи? (т/н): ").lower()
            if choice == 'т':
                print(f"Ваш складний пароль: {generate_advanced_password(user_length)}")
            else:
                print(f"Ваш базовий пароль: {generate_base_password(user_length)}")
        else:
            print("Довжина має бути більшою за нуль!")
    except ValueError:
        print("Помилка: введіть ціле число.")