#№3

#"Напишите функцию, которая генерирует случайную последовательность из 6 цифр,
# причем в этой последовательности должна быть как минимум одна цифра 3.
# Позиция 3 определяться случайным образом. Например: \"456379\" или \"033456\"."
import random


def ran():
    random_numbers = []
    for q in range(0,6):
        random_number = str(random.randint(1, 9)) 
        random_numbers.append(random_number)
    if '3' not in random_numbers:
        random_n = random.randint(0, 5)
        random_numbers[random_n] = '3'
    string_numbers = ''.join(random_numbers)
    print(string_numbers)
    
ran()

