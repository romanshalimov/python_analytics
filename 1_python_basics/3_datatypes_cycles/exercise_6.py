#Дана книга рецептов с информацией о том, сколько ингредиентов нужно для приготовления
#блюда в расчете на одну порцию. Напишите программу, которая будет запрашивать у пользователя
#количество порций для приготовления этих блюд и отображать информацию о суммарном количестве
#требуемых ингредиентов в указанном виде. Внимание! Одинаковые ингридиенты с разными размерностями нужно считать раздельно!

#дан словарь поваренной книги
cook_book = {
  'салат': [
     {'ingridient_name': 'сыр', 'quantity': 50, 'measure': 'гр'},
     {'ingridient_name': 'томаты', 'quantity': 2, 'measure': 'шт'},
     {'ingridient_name': 'огурцы', 'quantity': 20, 'measure': 'гр'},
     {'ingridient_name': 'маслины', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'оливковое масло', 'quantity': 20, 'measure': 'мл'},
     {'ingridient_name': 'салат', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'перец', 'quantity': 20, 'measure': 'гр'}
    ],
  'пицца': [
     {'ingridient_name': 'сыр', 'quantity': 20, 'measure': 'гр'},
     {'ingridient_name': 'колбаса', 'quantity': 30, 'measure': 'гр'},
     {'ingridient_name': 'бекон', 'quantity': 30, 'measure': 'гр'},
     {'ingridient_name': 'оливки', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'томаты', 'quantity': 20, 'measure': 'гр'},
     {'ingridient_name': 'тесто', 'quantity': 100, 'measure': 'гр'},   
    ],
  'лимонад': [
     {'ingridient_name': 'лимон', 'quantity': 1, 'measure': 'шт'},
     {'ingridient_name': 'вода', 'quantity': 200, 'measure': 'мл'},
     {'ingridient_name': 'сахар', 'quantity': 10, 'measure': 'гр'},
     {'ingridient_name': 'лайм', 'quantity': 20, 'measure': 'гр'},    
    ]
}

portions = int(input('Введите количество порций ')) #ввод порций
recipes = {} #создадим итоговый словарь рецептов

for dishes, ingredients in cook_book.items(): #переберём ключи-значения в словаре методом items


    for ingredient in ingredients: #переберём ингредиенты
        named = ingredient ['ingridient_name'] #создадим переменные названия, частей и количества ингредиентов
        dimension = ingredient ['measure']
        quantity = ingredient ['quantity']
        key = (named, dimension) #ключом словаря recipes будет имя и размерность
        value = recipes.get(key, 0) #а для получения значений применим метод get
        recipes [key] = portions * quantity + value #формула рецептов 
        
for ingridient_name, mass in recipes.items(): #переберём итоговый словарь рецептов применив метод items 
    print(f"{ingridient_name[0].capitalize()}: {mass} {ingridient_name[1]}") #выведем на экран результат расчёта смесей5