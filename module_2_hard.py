import random
n = random.randint(3,20)
print('Шифр: ',n)
result = []
password = ''
for i in range(1, 21):
    for j in range(1, 21):
        if i >= j:
            continue
        if n % (i+j) == 0:
            result.append([i, j])
            password = password + str(i) + str(j)
print('Введите пароль: ', password)
print('Свобода!')