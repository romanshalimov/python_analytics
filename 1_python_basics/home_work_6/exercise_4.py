#Ваш коллега прислал код функции:

#DEFAULT_USER_COUNT = 3
#def delete_and_return_last_user(region, default_list=[‘A100’, ‘A101’, ‘A102’]):
#""“
#Удаляет из списка default_list последнего пользователя и возвращает ID нового последнего пользователя.
#”""
#element_to_delete = default_list[-1]
#default_list.remove(element_to_delete)
#return default_list[DEFAULT_USER_COUNT-2]
#При однократном вызове этой функции всё работает корректно:
#delete_and_return_last_user(1)
#‘A101’
#Однако при повторном вызове получается ошибка IndexError: list index out of range.

#Задание:

#Что значит ошибка list index out of range?
#Почему при первом запуске функция работает корректно, а при втором — нет?

DEFAULT_USER_COUNT = 3

def delete_and_return_last_user(region, default_list=['A100', 'A101', 'A102']):
    """"
    Удаляет из списка default_list последнего пользователя
    и возвращает ID нового последнего пользователя.
    """
    element_to_delete = default_list[-1]
    default_list.remove(element_to_delete)

    return default_list[DEFAULT_USER_COUNT-2]

print(delete_and_return_last_user(1))
print(delete_and_return_last_user(1))

#1.Она обозначает попытку обратиться к элементу с номером, превышающим длину словаря - 1.
#2.Потому что функция использует список в качестве значения по умолчанию. Список изменяемый объект и после первого использования функции он изменяется. И при повторном вызове функции она использует укороченную версию значения по умолчанию.