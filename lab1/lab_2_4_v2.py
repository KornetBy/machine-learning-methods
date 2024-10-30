"""
Напишите программу, демонстрирующую работу try\except\finally
"""


try:
    number = int(input("Введите целое число: "))
    result = 10 / number 
    print(f"Результат деления 10 на {number}: {result}")

except ValueError:
    print("Ошибка: введено не целое число. Пожалуйста, введите корректное число")

except ZeroDivisionError:
    print("Ошибка: деление на ноль невозможно")

finally:
    print("Программа завершена")