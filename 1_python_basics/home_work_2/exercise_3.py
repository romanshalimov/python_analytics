boys = ["Svyatoslav", "Nestor", "Ivan", "Roman", "Konstantin"]
girls = ["Vasilisa", "Lubov", "Nadezhda", "Svetlana", "Mila"]

if len(boys) != len(girls):
  print('Внимание, кто-то может остаться без пары')
else:
  boys.sort() #сортируем
  girls.sort() 
  boys_and_girls = zip(girls, boys) #формируем кортеж
  for better_boys_and_girls in boys_and_girls:
    print(better_boys_and_girls[0], "и", better_boys_and_girls[1])