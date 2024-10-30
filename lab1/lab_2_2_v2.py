"""
Напишите функцию, которая будет принимать один аргумент. Если
в функцию передаётся кортеж, то посчитать его количество элементов.
Если список, то найти сумму до первого нулевого элемента.
Число – вывести его в обратном порядке.
Строка – кол-во слов. Определить какой символ в строке встречается
чаще всего.
Сделать проверку со всеми этими случаями
"""


def process_data(data):
    if isinstance(data, tuple):
        return f"Количество элементов в кортеже: {len(data)}"
    
    elif isinstance(data, list):
        sum_until_zero = 0
        for num in data:
            if num == 0:
                break
            sum_until_zero += num
        return f"Сумма элементов до первого нулевого элемента: {sum_until_zero}"
    
    elif isinstance(data, int):
        return f"Число в обратном порядке: {str(data)[::-1]}"
    
    elif isinstance(data, str):
        words = data.split()
        most_common_char = max(set(data), key=data.count)
        return f"Количество слов: {len(words)}, Самый частый символ: '{most_common_char}'"
    
    else:
        return "Неподдерживаемый тип данных"


while True:
    print("1. Обработать кортеж")
    print("2. Обработать список")
    print("3. Обработать число")
    print("4. Обработать строку")
    print("5. Выйти")

    choice = input("Введите номер действия: ")

    if choice == '1':
        user_input = input("Введите элементы кортежа через запятую: ")
        data = tuple(map(int,[item.strip() for item in user_input.split(',')]))
        print(process_data(data))
    
    elif choice == '2':
        user_input = input("Введите элементы списка через запятую: ")
        data = list(map(int, user_input.split(',')))
        print(process_data(data))
    
    elif choice == '3':
        user_input = int(input("Введите целое число: "))
        print(process_data(user_input))
    
    elif choice == '4':
        user_input = input("Введите строку: ")
        print(process_data(user_input))
    
    elif choice == '5':
        print("Выход из программы")
        break
    
    else:
        print("Некорректный ввод. Пожалуйста, выберите действие от 1 до 5")


