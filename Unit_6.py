import re

def strip_punctuation_ru(data):
    data = re.sub(r'[^\w\s]', '', data)
    data = re.sub(r'\s+', ' ', data).strip()
    return data

user_input = input("Введите предложение на русском языке: ")
cleaned_text = strip_punctuation_ru(user_input)
print(cleaned_text)