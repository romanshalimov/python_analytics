#№2
import re

some_string = "History is always written by the winners. When two cultures clash, the loser is obliterated, and the winner writes the history books - books which glorify their own cause and disparage the conquered foe. As Napoleon once said, 'What is history, but a fable agreed upon?'"

#"Напишите функцию, которая будет принимать в качестве аргумента букву и
# выводить все слова из строки, начинающиеся на эту букву (например, “w”)."

temp_string = input('Введите букву вначале слова: ')
print(re.findall(f"[\s]{temp_string[0]}[a-zA-Z]+|^{temp_string[0]}[a-zA-Z]+", some_string.lower()))









