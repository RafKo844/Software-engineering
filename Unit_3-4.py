import re
import sys

# задание 3

def is_correct_mobile_phone_number_ru(number):
    import re
    pattern = re.compile(r'^(8|\+7)[\-\s]?(?:\(\d{3}\)|\d{3})[\-\s]?\d{3}[\-\s]?\d{2}[\-\s]?\d{2}$')
    return bool(pattern.match(number))

def test_is_correct_mobile_phone_number_ru():
    test_cases = {
        "8(900)1234567": True,
        "+7(900)1234567": True,
        "+7 900 123 45 67": True,
        "8 900 123-45-67": True,
        "+7-900-123-45-67": True,
        "89001234567": True,
        "+79001234567": True,
        "+7(900)123-45-67": True,
        "8 900 123 45 67": True,
        "+7 900 123 45 6": False,  # Некорректное количество цифр
        "7 900 123 45 67": False,  # Неправильный префикс
        "9 900 123 45 67": False,  # Неправильный префикс
        "8(900)123456": False,     # Некорректное количество цифр
        "+7(900)123 45 678": False, # Слишком много цифр
        "8(90)01234567": False,    # Некорректный код оператора
    }
    for number, expected in test_cases.items():
        if is_correct_mobile_phone_number_ru(number) != expected:
            print("Результат задание №3: NO")
            return
    print("Результат задание №3: YES")

test_is_correct_mobile_phone_number_ru()

# задание 4
def is_correct_mobile_phone_number_ru(number):
    pattern = r'^(8|\+7)[\-\s]?(?:\(\d{3}\)|\d{3})[\-\s]?\d{3}[\-\s]?\d{2}[\-\s]?\d{2}$'
    return re.match(pattern, number) is not None
print("Введите номер телефона")
input_string = sys.stdin.readline().strip()

if is_correct_mobile_phone_number_ru(input_string):
    print("Результат задание №4: YES")
else:
    print("Результат задание №4: NO")
