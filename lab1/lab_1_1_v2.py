# Вывести на экран 1001 простое число
# Выводит все первые 1001 простое число

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = 2
index = 1
while index <= 1001:
    if is_prime(num):
        print(f'{index}-e простое число: {num}')
        index += 1
    num += 1


