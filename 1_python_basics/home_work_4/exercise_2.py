#1.код должен быть грамотно декомпозирован (каждая функция отвечает за свою конкретную задачу,
#дублирующийся функционал переиспользуется, а его код не повторяется);
#2.в коде отсутствуют глобальные переменные (за исключением documents и directories);
#3.пользовательский ввод обрабатывается в цикле while до тех пор, пока пользователь
#явно не завершит программу (вводом команды "q").

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

#Пользователь по команде "ad" может добавить новый документ в данные
def new_document ():
    """добавляет новый документ"""
    doc_num = input('Введите номер: ')
    doc_type = input('Введите тип: ')
    doc_owner = input('Введите владельца: ')
    doc_shelf = str(input('Введите полку: '))
    if doc_shelf not in directories:
        print("Такой полки нет")
    else:
        documents.append({'type':doc_type, 'number':doc_num,'name':doc_owner})
        directories[doc_shelf].append(doc_num)  
    return

#Пользователь по команде "d" может удалить документ из данных
def delete_document ():
    """удаляет документ"""
    doc_num = input("Введите номер документа на удаление: ")
    for docs in directories.values():
        if doc_num in docs:
            docs.remove(doc_num)
            print('Документ удалён.')
            break
    else:
        print('Такого документа нет в базе данных.')
        return
    for index, docs in enumerate(documents):
        if doc_num == docs['number']:
            documents.pop(index)
            break

#Пользователь по команде "m" может переместить документ с полки на полку
def moving_document ():
    """перемещает документ с полки на полку"""
    doc_number = input('Номер документа на перемещение: ')
    shelf = input('Номер полки назначения: ')
    for key, value in directories.items():
        if doc_number in value:
            value.remove(doc_number)
            for key, value in directories.items():
                if shelf in key:
                    value.append(doc_number)
    print(directories) 

def show_help():
    print('Список команд:')
    print('ad - добавляет новый документ')
    print('d - удаляет документ')
    print('m - перемещает документ с полки на полку')
    print('q- завершение программы')

def secretary_job ():
    show_help()
    
    while True:
        commands = input ('Введите команду: ')
        if commands == 'ad':
            new_document ()
        elif commands == 'd':
            delete_document ()
        elif commands == 'm':
            moving_document ()             
        elif commands == 'q':
            print ('Программа завершена.')
            break    
secretary_job ()