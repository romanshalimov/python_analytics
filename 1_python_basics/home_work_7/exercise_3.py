#Напишите класс Designer, который учитывает количество международных премий.

#Напишите класс Designer, который учитывает количество международных премий для дизайнеров
#(из презентации: “Повышение на 1 грейд за каждые 7 баллов. Получение международной премии – это +2 балла”).
#Считайте, что при выходе на работу сотрудник уже имеет две премии и их количество не меняется со стажем
#Класс Designer пишется по аналогии с классом Developer из материалов занятия.

class Employee:
    def __init__(self, name, seniority):
        self.name = name
        self.seniority = seniority
        
        self.grade = 1
    
    def grade_up(self):
        """Повышает уровень сотрудника"""
        self.grade += 1
    
    def publish_grade(self):
        """Публикация результатов аккредитации сотрудников"""
        print(self.name, self.grade)
    
    def check_if_it_is_time_for_upgrade(self):
        pass

class Designer(Employee):
    def __init__(self, name, seniority, awards):
        super().__init__(name, seniority)
        self.inter_prize = awards * 2
        self.seniority += self.inter_prize
    
    def check_if_it_is_time_for_upgrade(self):
        self.seniority += 1       
        if self.seniority % 7 == 0:
          self.grade_up()
        
        return self.publish_grade()

roman = Designer('Roman', seniority = 0, awards = 2)

for i in range(20):
    roman.check_if_it_is_time_for_upgrade()


