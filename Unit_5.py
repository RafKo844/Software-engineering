import re

def strip_punctuation_ru(data):
    # Удаляем все знаки препинания и лишние пробелы
    data = re.sub(r'[^\w\s]', '', data)
    data = re.sub(r'\s+', ' ', data).strip()
    return data


def test_strip_punctuation_ru():
    # Тестовые случаи
    tests = [
        ("Привет, мир!", "Привет мир"),
        ("Это тестовая строка.", "Это тестовая строка"),
        ("Много    пробелов!", "Много пробелов"),
        ("Ничего_не_должно_измениться", "Ничего_не_должно_измениться"),
        ("Специальные символы @#$%^&*() должны уйти!", "Специальные символы должны уйти"),
    ]

    # Проверка всех тестов
    for i, (input_data, expected_output) in enumerate(tests):
        result = strip_punctuation_ru(input_data)
        if result != expected_output:
            print(f"NO")
            return
    print("YES")

# Запуск тестов
test_strip_punctuation_ru()
