class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income
        self.salary_data = {'wage': income, 'bonus': income * 0.2}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self.salary_data['wage'] + self.salary_data['bonus'],'rub')


worker_1 = Position("Julio", "Jimenez", "corrector", 40000)
worker_1.get_full_name()
worker_1.get_total_income()
