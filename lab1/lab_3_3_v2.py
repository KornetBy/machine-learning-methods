"""
1. Реализуйте базовый класс Car.
2. У класса должны быть следующие атрибуты: speed, color, name, is_police
(булево). А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда);
3. Опишите несколько дочерних классов: TownCar, SportCar, WorkCar,
PoliceCar;
4. Добавьте в базовый класс метод show_speed, который должен показывать
текущую скорость автомобиля;
5. Для классов TownCar и WorkCar переопределите метод show_speed. При
значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться
сообщение о превышении скорости. 
"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f"{self.name} поехала.")

    def stop(self):
        print(f"{self.name} остановилась.")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}.")

    def show_speed(self):
        print(f"Текущая скорость {self.name}: {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"{self.name} превышает допустимую скорость! Текущая скорость: {self.speed} км/ч")
        else:
            super().show_speed()


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        
        if self.speed > 40:
            print(f"{self.name} превышает допустимую скорость! Текущая скорость: {self.speed} км/ч")
        else:
            super().show_speed()


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, is_police=True)


town_car = TownCar(65, "черный", "Машина")
sport_car = SportCar(120, "красный", "Спортивная машина")
work_car = WorkCar(45, "синий", "Рабочая")
police_car = PoliceCar(80, "белый", "Полицейская машина")


town_car.go()
town_car.show_speed()
town_car.turn("налево")
town_car.stop()

print()

sport_car.go()
sport_car.show_speed()
sport_car.turn("направо")
sport_car.stop()

print()

work_car.go()
work_car.show_speed()
work_car.turn("налево")
work_car.stop()

print()

police_car.go()
police_car.show_speed()
police_car.turn("направо")
police_car.stop()
