"""
Требуется написать программу, которая вычисляет общую площадь стен
комнаты, которую необходимо оклеить обоями. При этом окна, двери, пол и
потолок оклеивать не нужно
"""

class Room:
    def __init__(self, length, width, height, door_area, window_area):
        self.length = length
        self.width = width
        self.height = height
        self.door_area = door_area
        self.window_area = window_area

    def calculate_wall_area(self):
        total_wall_area = 2 * self.height * (self.length + self.width)
        return total_wall_area

    def calculate_area_to_cover(self):
        area_to_cover = self.calculate_wall_area() - (self.door_area + self.window_area)
        return area_to_cover

length = float(input("Введите длину комнаты (м): "))
width = float(input("Введите ширину комнаты (м): "))
height = float(input("Введите высоту комнаты (м): "))
door_area = float(input("Введите общую площадь дверей (м²): "))
window_area = float(input("Введите общую площадь окон (м²): "))

room = Room(length, width, height, door_area, window_area)

print(f"Общая площадь стен комнаты: {room.calculate_wall_area():.2f} м²")
print(f"Площадь для оклейки обоями (без окон и дверей): {room.calculate_area_to_cover():.2f} м²")
