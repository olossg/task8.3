# Напишите класс Designer, который учитывает количество международных премий для дизайнеров
# (из презентации: "Повышение на 1 грейд за каждые 7 баллов. Получение международной премии – это +2 балла").
# Считайте, что при выходе на работу сотрудник уже имеет две премии и их количество не меняется со стажем
# (конечно если хотите это можно вручную менять). Выполните проверку для 20 аккредитаций дизайнера Елены.
#

class Employee:
    def __init__(self, name, seniority, awards=None):
        self.name = name
        self.seniority = seniority
        self.grade = 1
        self.awards = awards

    def grade_up(self):
        """Повышает уровень сотрудника"""
        self.grade += 1

    def publish_grade(self):
        """Публикация результатов аккредитации сотрудников"""
        print(self.name, self.grade)


class Developer(Employee):
    def __init__(self, name, seniority):
        super().__init__(name, seniority)

    def check_if_it_is_time_for_upgrade(self):
        # для каждой аккредитации увеличиваем счетчик на 1
        # пока считаем, что все разработчики проходят аккредитацию
        self.seniority += 1

        # условие повышения сотрудника из презентации
        if self.seniority % 5 == 0:
            self.grade_up()

        # публикация результатов
        return self.publish_grade()

class Designer(Employee):
    def __init__(self, name, seniority, awards):
        super().__init__(name, seniority, awards)
        self.seniority = self.seniority + self.awards*2

    def check_if_it_is_time_for_upgrade(self):

        # для каждой аккредитации увеличиваем счетчик на 1
        # пока считаем, что все разработчики проходят аккредитацию
        self.seniority +=1

        # условие повышения сотрудника из презентации
        if self.seniority % 7 == 0:
            self.grade_up()

        # публикация результатов
        return self.publish_grade()

elena = Designer('Елена', seniority=0, awards=2)
for i in range(20):
    elena.check_if_it_is_time_for_upgrade()
print(elena)
