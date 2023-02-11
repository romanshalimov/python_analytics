#Создайте класс Student, который создает объекты с данными о студентах (как в задаче 4).
# Класс должен иметь следующие методы: add_to_dict (добавляет объект в словарь из задачи 4),
# update_dict (обновляет запись о студенте в словаре из задачи 4), change_group (изменяет номер группы студента),
# change_id (изменяет номер студента) и print_date (выводит на экран данные студента).

class Student:
    def __init__(self, s_id, last_name, first_name, patronomic_name, date, group):
        self.id = s_id
        self.last_name = last_name
        self.first_name = first_name
        self.patronomic_name = patronomic_name
        self.date = date
        self.group = group
            
    def add_to_dict(self):
        if self.id in students_dict.keys():
            print('Студент с таким номером уже существует')
        else:
            students_dict[self.id] = [self.last_name, self.first_name, self.patronomic_name, self.date, self.group]
               
    def update_dict(self):
        students_dict[self.id] = [self.last_name, self.first_name, self.patronomic_name, self.date, self.group]
        
    def change_group(self, new_group):
        self.group = new_group
        
    def change_id(self, new_id):
        self.id = new_id
        
    def print_data(self):
        print(f'{self.id} {self.last_name} {self.first_name} {self.patronomic_name} {self.date} {self.group}')
        
# 1. Создайте объект класса, добавьте его в словарь. Обновленный словарь выведете на экран.
volkova = Student('0001', 'Волкова', 'Галина', 'Сергеевна', '18.12.2022', 'БСТ100')
students_dict
volkova.print_data()
volkova.add_to_dict()
volkova.change_id('0002')
volkova.print_data()
volkova.add_to_dict()

students_dict

# 2. Измените номер группы студентки Волковой на 'БСТ161' и выведите обновленный список группы.

volkova.change_group('БСТ161')
volkova.update_dict()





















