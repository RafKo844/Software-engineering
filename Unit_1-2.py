import sys

# задание 1

def is_palindrome(data):
    return data == data[::-1]

def run_tests():
    test_cases = [
        ("мадам", True),
        ("комок", True),
        ("наган", True),
        ("правда", False),
        ("world", False),
        ("радар", True),
        ("потоп", True),
        ("12321", True),
        ("12345", False),
    ]
    
    for i, (input_str, expected) in enumerate(test_cases):
        result = is_palindrome(input_str)
        if result != expected:
            print(f"Test case {i+1} failed: {input_str}, expected {expected}, got {result}")
            return False
    return True

if run_tests():
    print("Результат задание №1: YES")
else:
    print("Результат задание №1: NO")

# задание 2

def is_palindrome(data):
    return data == data[::-1]
print("Введите текст")
input_string = sys.stdin.readline().strip()

if is_palindrome(input_string):
    print("Результат задание №2: YES")
else:
    print("Результат задание №2: NO")