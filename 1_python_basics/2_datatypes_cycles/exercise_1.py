word = input("Введите слово: ") #ввод слова

letters = int(len(word)/2) #переменная букв
if len(word)%2 == 0: #определение чётности
    print(word[letters-1:letters+1]) #средние две буквы
else:
    print(word[letters]) #средняя буква