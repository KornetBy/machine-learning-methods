"""
Создайте словарь из строки ' Enjoy every moment' следующим образом:
в качестве ключей возьмите символы строки, а значениями пусть
будут числа, соответствующие количеству вхождений данной буквы в
строку 
"""
string = ' Enjoy every moment'
char_count = {}

for char in string:
    if char in char_count:
        char_count[char] += 1  # Увеличиваем значение, если символ уже есть в словаре
    else:
        char_count[char] = 1   # Добавляем новый символ в словарь со значением 1

print(char_count)
