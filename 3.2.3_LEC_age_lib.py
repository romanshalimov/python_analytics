# coding: utf-8


def line_is_correct(line):
    """
    Проверяет корректность строки line по следующим правилам:
    - в строчке должно быть 3 столбца, разделенных запятыми
    - второе значение - целое число
    """
    values_list = line.split(',')
    
    if len(values_list) != 3:
        return False
    
    column_1, column_2, column_3 = values_list
    
    if not str.isnumeric(column_2):
        return False
    
    if not column_3.strip():
        return False
    
    return True


def military_case(age):
    """
    Возвращает возрастную категорию для возраста age по следующим правилам:
    - для age от 17 до 49 лет включительно категория 'военнослужащий'
    - младше 17 лет - категория 'не наш случай'
    - старше 50 лет - категория 'пенсионеры'
    - если age не целое число, то возвращает ValueError
    """
    if not isinstance(age, int):
        raise ValueError('Параметр age не целое число. Получил значение {} типа {}'.format(age, type(age)))

    if age <= 17:
        return 'не наш случай'
    elif age <= 49:
        return 'военнослужащий'
    else:
        return 'пенсионеры'
