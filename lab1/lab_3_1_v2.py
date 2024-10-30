"""
Класс Example. В нём пропишите 3 (метода) функции.
Две переменные задайте статически, две динамически.
Первый метод: создайте переменную и выведите её.
Второй метод: верните сумму 2-ух глобальных переменных.
Третий метод: верните результат возведения первой динамической
переменной во вторую динамическую переменную.
Создайте объект класса. Напечатайте оба метода. Напечатайте переменную a
"""


class Example:
    a = 10
    b = 20

    def __init__(self, dynamic_var1, dynamic_var2):
        self.dynamic_var1 = dynamic_var1
        self.dynamic_var2 = dynamic_var2

    def first_method(self):
        local_var = "Создание локальной переменной"
        print(local_var)

    def second_method(self):
        return Example.a + Example.b

    def third_method(self):
        return self.dynamic_var1 ** self.dynamic_var2

dynamic_var1 = int(input("Введите значение для dynamic_var1: "))
dynamic_var2 = int(input("Введите значение для dynamic_var2: "))

example = Example(dynamic_var1, dynamic_var2)

example.first_method()
print(f"Сумма глобальных переменных: {example.second_method()}")
print(f"Результат возведения в степень: {example.third_method()}")

print(f"Переменная a (global_var1): {Example.a}")
