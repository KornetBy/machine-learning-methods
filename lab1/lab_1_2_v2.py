"""
Вводится строка, содержащая буквы, целые неотрицательные числа и
иные символы. Требуется все числа, которые встречаются в строке
отдельно вывести на экран. Строка может содержать пробелы
"""


input_string = input("Введите строку: ")

number = ""
for char in input_string:
    if char.isdigit():  
        number += char
    elif number:  
        print(number)
        number = ""  
if number:  
    print(number)

