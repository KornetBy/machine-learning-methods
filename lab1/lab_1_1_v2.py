# Вывести на экран 1001 простое число
count = 0  
num = 2    

while count < 1001:
    is_prime = True 

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break 

    if is_prime:
        count += 1  

    if count < 1001:  
        num += 1

print("1001-е простое число:", num)



