class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')


class Pencil(Stationery):
    def draw(self):
        super().draw()


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} ручкой')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} от руки')


class Color(Stationery):
    def draw(self):
        super().draw()


thing_1 = Pencil("house")
thing_1.draw()
thing_2 = Pen("car")
thing_2.draw()
thing_3 = Handle("dog")
thing_3.draw()
thing_4 = Color("horse")
thing_4.draw()
