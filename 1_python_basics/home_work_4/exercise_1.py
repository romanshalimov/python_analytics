#Домашнее задание к лекции "Функции"
#нужно помочь секретарю автоматизировать работу. Для этого нужно написать программу,
#которая будет на основе хранимых данных исполнять пользовательские команды.

#требования к программе:
#1.код должен быть грамотно декомпозирован (каждая функция отвечает за свою конкретную задачу,
#дублирующийся функционал переиспользуется, а его код не повторяется);
#2.в коде отсутствуют глобальные переменные (за исключением documents и directories);
#3.пользовательский ввод обрабатывается в цикле while до тех пор, пока пользователь
#явно не завершит программу (вводом команды "q")

#перечень всех документов
documents = [
 {'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
 {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
 {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]

#перечень полок, на которых хранятся документы (если документ есть в documents,
#то он обязательно должен быть и в directories)
directories = {
 '1': ['2207 876234', '11-2'],
 '2': ['10006'],
 '3': []
}

#Пользователь по команде "p" может узнать владельца документа по его номеру
def owner ():
    """проверяет имя владельца по номеру документа"""
    numbers = input ('Введите номер документа: ')
    for number_doc in documents:
        if numbers == number_doc ['number']:
            print (f'Владелец документа: {number_doc["name"]}')
            break
    else:
        print ("Документ не найден")

#Пользователь по команде "s" может по номеру документа узнать, на какой полке он хранится
def shelf (numbers = None):
    """проверяет полку по номеру документа"""
    if numbers == None:
        numbers = input('Введите номер документа: ')
    for key, values in directories.items ():
        if numbers in values:
             desired_shelf = key
             print (f'Документ хранится на полке: {desired_shelf}')
             break
    else:
        print ("Документ не найден")

#Пользователь по команде "l" может увидеть полную информацию по всем документам
def all_information ():
    """выводит всю информацию"""
    for doc in documents:
        doc_type = doc.get('type')
        doc_number = doc.get('number')
        doc_name = doc.get('name')
        print (f'{doc_type} "{doc_number}" "{doc_name}"')

#Пользователь по команде "ads" может добавить новую полку
def shelf_list ():
    """вспомогательная функция"""
    shelf_list = ', '.join(shelf for shelf in directories)
    return str(shelf_list)

def newshelf ():
    """добавляет новую полку"""
    new_shelf = str(input('Введите номер полки: '))
    for shelfes in directories:
        if new_shelf in shelfes:
            print(f"Полка уже заполнена: {shelf_list()}")
            break
    else:
        directories[new_shelf] = []
        print(f"Полка добавлена: {shelf_list()}")

#Пользователь по команде "ds" может удалить существующую полку из данных (только если она пустая)
def shelf_delete ():
    """удаляет полку"""
    del_shelf = input('Введите номер полки: ')
    if del_shelf in directories:
        if directories[del_shelf]:
            print(f"""Полка уже заполнена: {shelf_list()}""")
        else:
            directories.pop(del_shelf)
            print(f"Полка удалена: {shelf_list()}")
    else: 
        print(f"Такой полки нет: {shelf_list()}")

def show_help():
    print('Список команд:')
    print('p - проверяет имя владельца по номеру документа')
    print('s - проверяет полку по номеру документа')
    print('l - выводит всю информацию')
    print('ads - добавляет новую полку')
    print('ds - удаляет полку')
    print('q- завершение программы')

def secretary_job ():
    show_help()
    
    while True:
        commands = input ('Введите команду: ')
        if commands == 'p':
            owner ()
        elif commands == 's':
            shelf ()
        elif commands == 'l':
            all_information ()           
        elif commands == 'ads':
            newshelf()
        elif commands == 'ds':
            shelf_delete()  
        elif commands == 'q':
            print ('Программа завершена.')
            break    
secretary_job ()