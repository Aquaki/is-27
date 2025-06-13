# Создание базового класса "Работник" и его наследование для создания классов
# "Менеджер" и "Инженер". В классе "Работник" будут общие методы, такие как
# "работать" и "получать зарплату", а классы-наследники будут иметь свои
# уникальные методы и свойства, такие как "управлять командой" и "проектировать
# системы"

class Employee:
    def __init__(self, name):
        self.name = name

    def work(self):
        print(f"{self.name} работает.")

    def receive_salary(self, amount):
        print(f"{self.name} получил зарплату {amount}.")


class Manager(Employee):
    def manage_team(self):
        print(f"{self.name}, менеджер, управляет своей командой.")


class Engineer(Employee):
    def design_systems(self):
        print(f"{self.name}, инженер, проектирует системы.")


# Тестируем базовые операции
john_doe = Employee("Иван")
john_doe.work()
john_doe.receive_salary(50_000)
print()

# Тестируем метод управления команды для менеджера
manager_jane = Manager("Сергей")
manager_jane.work()
manager_jane.manage_team()
manager_jane.receive_salary(75_000)
print()

# Тестируем проектирование систем инженером
engineer_mike = Engineer("Саша")
engineer_mike.work()
engineer_mike.design_systems()
engineer_mike.receive_salary(80_000)