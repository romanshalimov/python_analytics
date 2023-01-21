#Spyder IDE

#Домашнее задание

#1.Переведите содержимое файла purchase_log.txt в словарь purchases вида:
# {'1840e0b9d4': 'Продукты', ...}

#2.Для каждого user_id в файле visit_log.csv определите третий столбец с категорией покупки, если покупка была,
#сам файл visit_log.csv изменять не надо. Запишите в файл funnel.csv визиты из файла visit_log.csv, 
#в которых были покупки, с указанием категории.
# Учтите условия на данные: содержимое purchase_log.txt помещается в оперативную память компьютера;
#содержимое visit_log.csv — нет; используйте только построчную обработку этого файла.

with open('purchase_log.txt','r', encoding='utf-8') as log: #откроем файл в необходимой кодировке
    import json #импортируем библиотеку
    new_log = [] #создадим пустой список
    for line in log: #переберём строки в нашем файле
        line = line.strip() #применим метод strip для удаления начальных и конечных символов
        jsoned_log = json.loads(line) #приведём наши строки к Python-формату
        new_log.append(jsoned_log) #добавим в пустой список new_log приведённые строки
    log.close() #закроем наш файл, так как мы извлекли из него всё необходимое и он нам больше не нужен
purchases_dictionary = {} #создадим пустой словарь (находиться в оперативной памяти)
for logs in new_log:
    purchases_dictionary[logs['user_id']] = logs['category'] #наполним наш словарь извлечёнными данными

with open('visit_log.csv', 'r', encoding='utf-8') as visit: #откроем наш файл для чтения
    with open('funnel.csv', 'w', encoding='utf-8') as funnel: #создадим новый файл funnel.csv
        for line in visit: #переберём строки в нашем файле
            line = line.strip().split(',') #применим методы strip и split, разбив по запятым на подстроки
            if line[0] in purchases_dictionary.keys(): #если user_id в наших сущностях совпадают
                line.append(purchases_dictionary[line[0]]) #соединим наши сущности исключая user_id
                funnel.write(','.join(line)+"\n") #запишем наши данные в файл funnel.csv применив метод join
    visit.close() #закрываем файлы
    funnel.close()
    
    
    
    
    
    
    
    
    
    
    
    