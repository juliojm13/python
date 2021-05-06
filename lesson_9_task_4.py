class Car:
    def __init__(self, speed, color, name, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print(f'{self.name} is going')

    def stop(self):
        print(f'{self.name} stopped')

    def turn(self, dirrection):
        print(f'{self.name} turned to the {dirrection}')

    def show_speed(self):
        print(f'{self.name} is going with the speed of {self.speed} km/h')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.name} is going too fast with the speed of {self.speed}')
        else:
            print(f'{self.name} is going with the speed of {self.speed} km/h')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.name} is going too fast with the speed of {self.speed}')
        else:
            print(f'{self.name} is going with the speed of {self.speed} km/h')


class PoliceCar(Car):
    pass


car_1 = TownCar(70, 'red', 'Lambo', False)
car_1.go()
car_1.show_speed()
car_1.turn("right")
car_2 = SportCar(70, 'black', 'Lambo', False)
car_2.go()
car_2.show_speed()
car_2.stop()
car_3 = WorkCar(45, 'red', 'Nissan', False)
car_3.show_speed()
car_4 = WorkCar(30, 'blue', 'Nissan', False)
car_4.show_speed()
car_5 = PoliceCar(100, 'white', 'BMW', True)
car_5.show_speed()
