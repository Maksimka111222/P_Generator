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

def check_password_strength(password):
    if len(password) >= 8 and any(c.isdigit() for c in password) and any(c in string.punctuation for c in password):
        return "Надійний"
    return "Слабкий"

if __name__ == "__main__":
    print("--- Генератор паролів ---")
    try:
        user_length = int(input("Введіть довжину пароля (наприклад, 8): "))
        if user_length > 0:
            choice = input("Використовувати цифри та спецсимволи? (т/н): ").lower()
            if choice == 'т':
                pwd = generate_advanced_password(user_length)
                print(f"Ваш складний пароль: {pwd}")
                print(f"Статус надійності: {check_password_strength(pwd)}")
            else:
                pwd = generate_base_password(user_length)
                print(f"Ваш базовий пароль: {pwd}")
                print(f"Статус надійності: {check_password_strength(pwd)}")
        else:
            print("Довжина має бути більшою за нуль!")
    except ValueError:
        print("Помилка: введіть ціле число.")
