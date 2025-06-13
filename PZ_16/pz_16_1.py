# Создайте класс «Счетчик», который имеет атрибут текущего значения и методы для
# инкремента и декремента значения

class Counter:
    def __init__(self, initial_value=0):
        self.value = initial_value

    def increment(self):
        # Увеличивает значение счетчика на 1.
        self.value += 1

    def decrement(self):
        # Уменьшает значение счетчика на 1.
        if self.value > 0:
            self.value -= 1

    def print_value(self):
        # Отображает текущее значение счетчика.
        print(f"Текущее значение счетчика: {self.value}")


if __name__ == "__main__":
    counter = Counter(initial_value=5)

    counter.print_value()

    # Инкрементируем значение один раз
    counter.increment()
    counter.print_value()

    # Декрементируем значение один раз
    counter.decrement()
    counter.print_value()

