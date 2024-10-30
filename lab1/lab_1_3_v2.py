"""
Введите одномерный целочисленный список. Найдите наибольший 
нечетный элемент. Найдите минимальный по модулю элемент списка
"""

int_list = []
print("Введите целые числа. Для завершения ввода введите '!'.")

while True:
    user_input = input("Введите число: ")
    if user_input == '!':
        break
    try:
        number = int(user_input)
        int_list.append(number)  
    except ValueError:
        print("Пожалуйста, введите корректное целое число или '!' для завершения ввода.")

if not int_list:
    print("Список пуст. Пожалуйста, введите хотя бы одно число.")
else:  

    largest_odd = None
    for num in int_list:
        if num % 2 != 0:  
            if largest_odd is None or num > largest_odd:
                largest_odd = num

    print(f"Наибольший нечетный элемент: {largest_odd if largest_odd is not None else 'Не найдено'}")
    
    min_abs = int_list[0]
    for num in int_list:
        if abs(num) < abs(min_abs):
            min_abs = num
    print(f"Минимальный по модулю элемент: {min_abs}")